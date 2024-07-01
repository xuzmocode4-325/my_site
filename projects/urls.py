from django.urls import path
from . import views

urlpatterns = [
    path("", views.projects, name="projects"), 
    path("<slug:slug>", views.project, name="single_project")
]