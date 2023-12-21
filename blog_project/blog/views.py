from django.shortcuts import render
from django.http import HttpResponse
from datetime import date

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
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "John",
        "date": date(2022, 3, 10),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit.
          Officiis nobis aperiam est praesentium, quos is consequuntur omnis exercitationem quam.
          Velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Mary",
        "date": date(2020, 8, 5),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit.
          Officiis nobis aperiam est praesentium, quos is consequuntur omnis exercitationem quam.
          Velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    }
]


def get_date(post):
    return post['date']


def home(request):
    """
    This is the home view function.
    It returns an HTTP response.
    """
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]

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

##