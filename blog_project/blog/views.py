from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    """
    This is the home view function.
    It returns an HTTP response.
    """
    return HttpResponse("<h1>Hello, Django!</h1>")
    # return render(request, 'home.html', {})

def posts(request):
    """
    This is the posts view function.
    It returns an HTTP response.
    """
    return HttpResponse("<h1>Hello, Posts Page!</h1>")

def posts_detail(request, slug):
    """
    This is the posts_detail view function.
    It returns an HTTP response.
    """
    return HttpResponse(f"<h1>Hello, Post Detail Page! - {slug}</h1>")
