from django.urls import path
from . import views

urlpatterns = [
    path("", 
        views.BlogHomeView.as_view(), 
        name="blog"), 
    path("posts/", 
        views.BlogPostsView.as_view(), 
        name="all-posts"),
    path("posts/<slug:slug>", 
        views.BlogDetailView.as_view(), 
        name="single-post-page"),
]