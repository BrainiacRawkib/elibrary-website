import stripe
# import cloudinary
from cloudinary import uploader

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.http import FileResponse, HttpResponse
from django.contrib import messages

from django_downloadview import HTTPDownloadView, StorageDownloadView
from ratelimit.decorators import ratelimit

from .models import Category, Book
from .forms import AddBookForm, EditBookForm

from .models import DownloadHistory


# stripe.api_key = settings.STRIPE_TEST_SECRET_KEY


# def rate_based_on_donation(request):
#     customers = stripe.checkout.Session.list(expand=['data.customer'], limit=5)
#     d = [i.customer for i in customers.data if i.payment_status == 'paid']
#     if request.user.is_authenticated:
#         if request.user.email in d:
#             return '3/d'
#         return redirect('donations:donate')


@login_required
# @ratelimit(key='ip', rate='10/d', method=['GET'], block=True)
def download(request, title, isbn):
    book = get_object_or_404(Book, title=title, isbn=isbn).file.url
    # response = FileResponse(open(book, 'rb'), as_attachment=True)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename={book}'
    if request.method == 'GET':
        downloads = DownloadHistory(user=request.user, book_id=Book.objects.get(title=title, isbn=isbn))
        downloads.save()
    return response


class Download(StorageDownloadView):
    def get_file(self):
        book = get_object_or_404(Book, title=self.kwargs.get('title'), isbn=self.kwargs.get('isbn')).file.url
        downloads = DownloadHistory(user=self.request.user, book_id=Book.objects.get(title=self.kwargs.get('title'), isbn=self.kwargs.get('isbn')))
        downloads.save()
        return book


def categories(request, id=None, slug=None):
    category = None
    all_categories = Category.objects.order_by('name')
    books = Book.objects.all()
    if id and slug:
        category = get_object_or_404(Category, id=id, slug=slug)
        books = books.filter(category=category)
    context = {
        'title': 'Categories',
        'category': category,
        'categories': all_categories,
        'books': books
    }
    return render(request, 'books/categories.html', context)


def book_detail(request, title, isbn):
    book = get_object_or_404(Book, title=title, isbn=isbn)
    context = {
        'title': f'{book.title}',
        'book': book,
    }
    return render(request, 'books/book_detail.html', context)


@login_required
@permission_required('books.add_category', raise_exception=True)
def add_category(request):
    if request.method == "POST":
        name = request.POST['category_name']
        slug = request.POST['category_slug']
        category = Category(name=name, slug=slug)
        category.save()
        return redirect('books:categories')


@login_required
@permission_required('books.add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = AddBookForm(request.POST, files=request.FILES)
        if form.is_valid():
            # uploader.upload(str(form.instance.file.path))
            form.save()
            messages.success(request, f'Book Added Successfully')
            return redirect('home:index')
    else:
        form = AddBookForm()
    context = {
        'title': 'Add Book',
        'form': form
    }
    return render(request, 'books/add_book.html', context)


@login_required
@permission_required('books.edit_book', raise_exception=True)
def edit_book(request, title, isbn):
    book = get_object_or_404(Book, title=title, isbn=isbn)
    if request.method == 'POST':
        form = EditBookForm(request.POST, files=request.FILES, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, f'{book.title} Edited Successfully')
            return redirect('home:index')
    else:
        form = EditBookForm(instance=book)
    context = {
        'title': f'Edit {book.title}',
        'form': form
    }
    return render(request, 'books/edit_book.html', context)


@login_required
@permission_required('books.delete_book', raise_exception=True)
def delete_book(request, title, isbn):
    book = get_object_or_404(Book, title=title, isbn=isbn)
    if request.method == "POST":
        del_book = get_object_or_404(Book, title=title, isbn=isbn)
        del_book.delete()
        messages.success(request, f'{book.title} Deleted')
        return redirect('home:index')
    context = {
        'title': f'Delete {book.title}',
        'book': book
    }
    return render(request, 'books/delete_book.html', context)
