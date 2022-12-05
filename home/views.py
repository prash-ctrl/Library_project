from django.shortcuts import render, redirect
from . forms import  AddBookForm, AuthorModelForm
from . models import Books, Author, Contact
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import folium 
import geocoder
# Create your views here.


def home(request):
    m= folium.Map(location=[28, 84] , zoom_start=7)
    folium.Marker([28, 85]).add_to(m)
    m = m._repr_html_()
    context = {
        'm' : m,
    }
    return render(request, 'home.html', context)

def contact(request):
    return render(request, 'contact.html')

def location(request):
    m= folium.Map(location=[28, 84] , zoom_start=7)
    folium.Marker([28, 85]).add_to(m)
    m = m._repr_html_()
    context = {
        'm' : m,
    }
    return render(request, 'location.html', context)

def list_book(request):
    books =Books.objects.all()
    return render(request, 'list_book.html', context={'books':books})

@login_required
def add_book(request):
    if request.method == 'GET':
        book_add_form = AddBookForm()
        return render(request, 'add_book.html', context={'form': book_add_form})

    else:
        book_add_form = AddBookForm(request.POST)
        if book_add_form.is_valid():
            book_add_form.save()
            return redirect('list_book')
    return render(request, 'add_book.html', context={'form': book_add_form})


@login_required
def edit_books(request, id):
    books = Books.objects.get(id=id)
    if request.method == "GET":
        form = AddBookForm(instance=books)
        return render(request, 'edit_book.html', context={'form': form})

    elif request.method == "POST":

        form = AddBookForm(request.POST, instance=books)
        if form.is_valid():
            form.save()
            return redirect('list_book')
    return render(request, 'edit_book.html', context={'form': form})


@login_required
def delete_books(request, id):
    books = Books.objects.get(id=id)
    books.delete()
    return redirect('list_book')


@login_required
def add_author(request):
    if request.method == 'GET':
        author_add_form = AuthorModelForm()
        return render(request, 'add_author.html', context={'form': author_add_form})

    else:
        author_add_form = AuthorModelForm(request.POST)
        if author_add_form.is_valid():
            author_add_form.save()
            return redirect('home')
    return render(request, 'add_author.html', context={'form': author_add_form})

def chart(request):
    book = Books.objects.all()
    return render(request, 'chart.html', {'book': book})