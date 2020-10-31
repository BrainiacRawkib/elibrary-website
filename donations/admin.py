from django.contrib import admin
from .models import Donor


@admin.register(Donor)
class DonorAdmin(admin.ModelAdmin):
    list_display = ['id', 'donor', 'amount', 'paid']
    list_display_links = ['id', 'donor']
    list_per_page = 10
