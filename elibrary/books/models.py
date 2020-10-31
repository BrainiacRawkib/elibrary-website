import os

from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User

from cloudinary.models import CloudinaryField
from cloudinary_storage.storage import RawMediaCloudinaryStorage


class Category(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def get_absolute_url(self):
        return reverse('books:categorized-books', kwargs={'id': self.id, 'slug': self.slug})

    def __str__(self):
        return f'{self.name}'


class Book(models.Model):
    isbn = models.IntegerField(unique=True)
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.CharField(max_length=150, default='')
    publisher = models.CharField(max_length=60, default='')
    # file = models.FileField(upload_to='raw/books/%Y/%m/%d/', storage=RawMediaCloudinaryStorage())
    file = models.FileField(upload_to='raw/books/%Y/%m/%d/', storage=RawMediaCloudinaryStorage())
    cover = models.ImageField(default='default_cover.jpg', upload_to='images/books_cover_page/%Y/%m/%d/')
    edition = models.CharField(max_length=15)
    pages = models.IntegerField('Number of Pages')
    language = models.CharField(max_length=20)
    pub_year = models.DateField('Year Published')
    summary = models.TextField('Book Summary')

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def extension(self):
        base, ext = os.path.splitext(self.file.name)
        return ext

    def size(self):
        file_size = os.path.getsize(self.file.path)
        return file_size

    def get_absolute_url(self):
        return reverse('books:book-detail', args=[self.title, self.isbn])

    def __str__(self):
        return f'{self.title}'


class DownloadHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} {self.book_id.title}'
