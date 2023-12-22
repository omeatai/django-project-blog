from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
from .models import Post, Author, Tag

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Jimmy",
        "date": date(2021, 7, 21),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit.
          Officiis nobis aperiam est praesentium, quos is consequuntur omnis exercitationem quam.
          Velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },

]

def home(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, 'blog/index.html', {
        "posts": latest_posts
    })


def posts(request):
    """
    This is the posts view function.
    It returns an HTTP response.
    """
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })


def posts_detail(request, slug):
    """
    This is the posts_detail view function.
    It returns an HTTP response.
    """
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post,
    })
