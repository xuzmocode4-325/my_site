from django.shortcuts import render

# Create your views here.

def projects(requests):
    return render(requests, "projects/index.html")