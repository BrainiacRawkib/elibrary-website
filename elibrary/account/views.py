from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']

            if User.objects.filter(username=username).exists():
                messages.error(request, f'Username already exists')
            elif User.objects.filter(email=email).exists():
                messages.error(request, f'Email already exists')
            else:
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                current_site = get_current_site(request)
                mail_subject = 'Activate your account.'
                activation_context = {
                    'user': user,
                    'domain': current_site,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': default_token_generator.make_token(user)
                }
                msg = render_to_string('account/activate_account_email.html', activation_context)
                to_email = email
                send_email = EmailMessage(mail_subject, msg, to=[to_email])
                send_email.send()
                messages.info(request, 'Please Confirm Your Email Address.')
                return redirect('home:index')
    else:
        form = UserRegistrationForm()
    context = {
        'form': form,
        'title': 'Sign Up'
    }
    return render(request, 'account/register.html', context)


UserModel = get_user_model()


def activate_account(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Account Activated Successfully. You Can Now Login')
        return redirect('account:login')
    else:
        messages.error(request, 'Invalid Activation Link')
        return redirect('home:index')


@login_required
def dashboard(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, instance=request.user.profile, files=request.FILES)

        if u_form.is_valid() and p_form.is_valid():
            username = u_form.cleaned_data['username']
            email = u_form.cleaned_data['email']

            if email != User.objects.exclude(email=email):
                u_form.save()
                p_form.save()
                messages.success(request, f'Account Successfully Updated!!!')
                return redirect('account:dashboard')
        else:
            messages.error(request, f'Email already exists')
            return redirect('account:dashboard')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'title': "Dashboard",
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'account/dashboard.html', context)


@login_required
def delete_account(request):
    if request.method == 'POST':
        account = User.objects.get(id=request.user.id)
        account.delete()
        messages.success(request, f'{account.username}\'s Account Successfully Deleted')
        return redirect('home:index')
    context = {
        'title': 'Delete Account'
    }
    return render(request, 'account/delete_account.html', context)
