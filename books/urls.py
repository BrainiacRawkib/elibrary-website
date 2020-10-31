from django.urls import path
from .views import Download
from . import views


app_name = 'books'


urlpatterns = [
    path('categories/', views.categories, name='categories'),
    path('add-book/', views.add_book, name='add-book'),
    path('add-category/', views.add_category, name='add-category'),
    path('download/<str:title>/<int:isbn>/', views.download, name='download'),
    # path('download/<str:title>/<int:isbn>/', Download.as_view(), name='download'),
    path('categories/<int:id>/<slug:slug>/', views.categories, name='categorized-books'),
    path('book-detail/<str:title>/<int:isbn>/', views.book_detail, name='book-detail'),
    path('edit-book/<str:title>/<int:isbn>/', views.edit_book, name='edit-book'),
    path('delete-book/<str:title>/<int:isbn>/', views.delete_book, name='delete-book')
]
