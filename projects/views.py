from django.shortcuts import render

# Create your views here.

def projects(requests):
    return render(requests, "projects/index.html")

def single_projects(requests, slug):
    return render(requests, "projects/single_project.html")