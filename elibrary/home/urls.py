from django.urls import path
from . import views
from .views import IndexView


app_name = 'home'


urlpatterns = [
    # path('', views.index, name='index'),
    path('', IndexView.as_view(), name='index'),
    path('search', views.search, name='search'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact')
]
