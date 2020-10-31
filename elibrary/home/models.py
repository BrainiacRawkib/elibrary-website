from django.db import models
from django.utils import timezone


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    contact_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.name}'


# class SocialLink(models.Model):
#     url = models.URLField()
#
#     def __str__(self):
#         return f'{self.url}'
