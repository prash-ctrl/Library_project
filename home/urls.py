from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('location/', views.location, name='location'),
    path('list-book/',views.list_book, name='list_book'),
    path('add-book/',views.add_book, name='add_book'),
    path('add-author/',views.add_author, name='add_author'),
    path('edit-books/<int:id>/',views.edit_books, name='edit-books'),
    path('delete-books/<int:id>/', views.delete_books, name='delete-books'),
    path('chart/', views.chart, name='chart')

]