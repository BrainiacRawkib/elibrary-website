from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    photo = models.ImageField(default='avatar.png', upload_to='photos/%Y/%m/%d/')

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return f'{self.user.username}'
