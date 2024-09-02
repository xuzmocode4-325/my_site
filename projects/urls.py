from django.urls import path
from . import views

urlpatterns = [
    path("", 
        views.ProjectsHomeView.as_view(), 
        name="projects"), 
    path("gallery", 
        views.ProjectsGalleryView.as_view(), 
        name="projects-gallery-page"),
    path("<slug:slug>", 
        views.ProjectDetailView.as_view(), 
        name="single-project-page")
]