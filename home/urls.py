from django.urls import path
from . import views

urlpatterns = [
    path("", 
        views.StartingPageView.as_view(), 
        name="home"), 
    path("about", 
        views.AboutPageView.as_view(), 
        name="about"),
    path("contact", 
        views.ContactPageView.as_view(), 
        name="contact"),
]