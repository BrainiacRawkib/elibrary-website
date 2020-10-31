from datetime import date

from django import forms

from .models import Book
from tinymce.widgets import TinyMCE


PUBLISHER_YEAR = [i for i in range(2000, date.today().year + 1)]


class AddBookForm(forms.ModelForm):
    pub_year = forms.DateField(label='Year of Publication', widget=forms.SelectDateWidget(years=PUBLISHER_YEAR))
    summary = forms.CharField(widget=TinyMCE())

    class Meta:
        model = Book
        fields = ['isbn', 'title', 'category', 'cover', 'file', 'author', 'publisher', 'edition', 'pages',
                  'language', 'pub_year', 'summary']


class EditBookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ['isbn', 'title', 'category', 'cover', 'file', 'author', 'publisher', 'edition']
