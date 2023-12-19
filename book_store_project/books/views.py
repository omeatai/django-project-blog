from django.shortcuts import get_object_or_404, render
from django.http import Http404

from .models import Book

# Create your views here.


def index(request):
    books = Book.objects.all()  # Retrieve all books from the database
    # print(books)
    return render(request, "books/index.html", {"books": books})


def book_details(request, slug):
    # try:
    #     book = Book.objects.get(pk=id)
    # except Book.DoesNotExist:
    #     raise Http404("Book does not exist")
    book = get_object_or_404(Book, slug=slug)
    return render(request, "books/book_details.html", {
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_bestselling": book.is_bestselling,
    })
