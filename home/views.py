import os

from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.core.mail import send_mail
from django.contrib import messages
from .models import Contact

from books.models import Book


def index(request):
    books = Book.objects.all()
    context = {
        'title': 'Home',
        'books': books,
    }
    return render(request, 'home/index.html', context)


class IndexView(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'home/index.html'
    paginate_by = 20
    extra_context = {'title': 'Home'}
    ordering = ['-pub_year']


def search(request):
    queryset_list = Book.objects.all()
    if 'keywords' in request.GET:
        keywords = request.GET.get('keywords')
        if keywords:
            queryset_list = queryset_list.filter(Q(title__icontains=keywords) | Q(isbn__icontains=keywords))
    context = {
        'title': 'Search',
        'values': request.GET,
        'results': queryset_list,
    }
    return render(request, 'home/search.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST['email']
        message = request.POST.get('message')

        msg = Contact(name=name, email=email, message=message)
        msg.save()
        send_mail('Message from Library - Pro', 'A message has been sent to the Admin from the users of Library-Pro',
                  os.environ.get('EMAIL_HOST_USER'), [os.environ.get('EMAIL_HOST_USER'), 'techguy@tech.com'], fail_silently=False)
        messages.success(request, 'Your message has been sent.')
        return redirect('home:index')

    context = {
        'title': 'Contact'
    }
    return render(request, 'home/contact.html', context)


def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'home/about.html', context)
