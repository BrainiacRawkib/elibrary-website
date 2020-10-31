from django.contrib import admin
from django.db import models

from tinymce.widgets import AdminTinyMCE
from .models import Category, Book, DownloadHistory


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'publisher', 'category', 'isbn']
    list_display_links = ['id', 'title']
    formfield_overrides = {models.TextField: {'widget': AdminTinyMCE()}}


@admin.register(DownloadHistory)
class DownloadHistoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'book_id']
    list_display_links = ['id', 'user', 'book_id']
    list_filter = ['user', 'book_id']
