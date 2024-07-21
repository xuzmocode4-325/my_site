from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from datetime import date
from .models import Post

# Create your views here.

def get_date(item):
    return item["date"]


def blog(request): 
    latest_posts = Post.objects.all().order_by("-created_at")
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    articles = Post.objects.all().order_by("-created_at")
    return render(request, "blog/posts.html", {
        "posts": articles
    })

def single_post(request, slug):
    post =  Post.objects.get(slug=slug) 
    return render(request, "blog/single-post.html", {
        "post": post,
        "tags": post.tag.all()
    })