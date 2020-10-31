from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from account.models import Profile


class Donor(models.Model):
    donor = models.ForeignKey(Profile, related_name='donors', on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
    amount = models.PositiveIntegerField()
    date = models.DateField(default=now)

    class Meta:
        verbose_name_plural = 'Donors'

    def __str__(self):
        return f'{self.donor}'
