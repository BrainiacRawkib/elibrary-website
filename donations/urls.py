from django.urls import path
from .views import SuccessView, ErrorView
from . import views


app_name = 'donations'


urlpatterns = [
    path('donors/', views.donors, name='donors'),
    path('donate/', views.donate, name='donate'),
    path('one-time/', views.one_time, name='one-time'),
    path('recurring/', views.recurring, name='recurring'),
    path('get-session/', views.get_session, name='get-session'),
    path('success/', SuccessView.as_view(), name='successful'),
    path('error/', ErrorView.as_view(), name='error'),
    path('webhook/', views.webhook, name='webhook'),
]
