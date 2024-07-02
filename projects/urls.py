from django.urls import path
from . import views

urlpatterns = [
    path("", views.projects_index, name="projects"), 
    path("gallery", views.projects_gallery, name="projects-gallery-page"),
    path("<slug:slug>", views.single_project, name="single-project-page")
]