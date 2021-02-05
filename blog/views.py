from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

posts = [
    {
        "author": "Indra",
        "title": "Post 1",
        "content": "Test content",
        "date_posted": "Jan 29",
    },
    {
        "author": "Kurniawan",
        "title": "Post 2",
        "content": "Test content 2",
        "date_posted": "Jan 31",
    },
]


def home(request):
    context = {"posts": Post.objects.all()}
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", {"title": "About"})
