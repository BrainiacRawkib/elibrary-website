from django.urls import path
from django.urls import reverse_lazy, reverse, resolvers
from django.contrib.auth import views as auth_views
from . import views

app_name = 'account'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('delete-account/', views.delete_account, name='delete-account'),
    path('activate/<uidb64>/<token>/', views.activate_account, name='activate-activate'),
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html', extra_context={'title': 'Login'}),
         name='login'),
    path('logout/',
         auth_views.LogoutView.as_view(template_name='account/logout.html', extra_context={'title': 'Logout'}),
         name='logout'),

    # change password
    path('password-change/',
         auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('account:password_change_done'),
                                               extra_context={'title': 'Change Password'}),
         name='password_change'
    ),
    path('password-change/done/',
         auth_views.PasswordChangeDoneView.as_view(),
         name='password_change_done'
    ),

    # reset password
    path('password-reset/',
         auth_views.PasswordResetView.as_view(success_url=reverse_lazy('account:password_reset_done'),
                                              extra_context={'title': 'Reset Password'}),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
                                                  extra_context={'title': 'Done'}),
         name='password_reset_done'
         ),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('account:password_reset_complete'),
                                                     extra_context={'title': 'Confirm'}),
         name='password_reset_confirm'
         ),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
                                                                     extra_context={'title': 'Complete'}),
         name='password_reset_complete'
         )
]
