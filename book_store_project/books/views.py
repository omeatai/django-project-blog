from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.db.models import Avg, Min, Max, Count, Sum
from .models import Book

# Create your views here.


def index(request):
    books = Book.objects.all().order_by("-rating","title")  # Retrieve all books and Order from the database
    num_books = books.count()  # Count the number of books
    aggregated_rating = books.aggregate(average_rating=Avg("rating"), min_rating=Min("rating"), max_rating=Max("rating"), count_rating=Count("rating"), sum_rating=Sum("rating"))  # Calculate on the rating

    return render(request, "books/index.html", {
        "books": books,
        "total_number_of_books": num_books,
        "aggregated_rating": aggregated_rating,
    })


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
