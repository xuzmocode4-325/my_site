from typing import Any
from django.views.generic import ListView, TemplateView, DetailView
from .models import Project
from .forms import ReviewForm
# Create your views here.


class ProjectsHomeView(TemplateView):
    template_name = "projects/index.html"

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context["projects"] = Project.objects.all().order_by('-created_at')[:9]
        context["featured"] = Project.objects.filter(
            tag__caption="featured").order_by('-created_at')[:1]
        return context


class ProjectsGalleryView(ListView):
    template_name = "projects/gallery.html"
    model = Project
    context_object_name = "projects"


class ProjectDetailView(DetailView):
    template_name = "projects/single-project.html"
    model = Project
    context_object_name = "project"
