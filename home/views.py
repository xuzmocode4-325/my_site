from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from datetime import date
from blog.models import Post
# Create your views here.


def get_date(item):
    return item["date"]

def home(request): 
    latest_posts = Post.objects.all().order_by("-created_at")[:3]
    return render(request, "home/index.html",  {
        "posts": latest_posts
    })

def about(request):
    return render(request, "home/about.html")

def contact(request):
    return render(request, "home/contact.html")
