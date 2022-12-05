from django import forms
from . models import Books, Author


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = '__all__'


class AuthorModelForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
