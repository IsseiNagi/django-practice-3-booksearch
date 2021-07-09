from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book

# Create your views here.


class BookList(ListView):
    template_name = 'list.html'
    model = Book


class BookDetailView(DetailView):
    template_name = 'detail.html'
    model = Book
