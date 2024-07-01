from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog, name="blog"), 
    path("posts", views.posts, name="all-posts"),
    path("posts/<slug:slug>", views.single_post, name="single-post-page"),
]