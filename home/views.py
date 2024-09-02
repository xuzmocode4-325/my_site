from django.views.generic import TemplateView
from blog.models import Post
from projects.models import Project
# Create your views here.

class StartingPageView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all().order_by('-created_at')[:3]
        context["projects"] = Project.objects.all().order_by('-created_at')[:3]
        return context


class AboutPageView(TemplateView):
    template_name = "home/about.html"


class ContactPageView(TemplateView):
    template_name = "home/contact.html"
