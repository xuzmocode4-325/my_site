from typing import Any
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import ListView, TemplateView, DetailView
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import CommentForm

# Create your views here


class BlogHomeView(TemplateView):
    template_name = "blog/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all().order_by('-created_at')[:9]
        return context


class BlogPostsView(ListView):
    template_name = "blog/posts.html"
    model = Post
    context_object_name = "posts"


class BlogDetailView(View):
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        post_comments = post.post_comments.all().order_by("-created_at") 
        context = {
            "post": post,
            "post_tags": post.tag.all(),
            "comment_form": CommentForm(),
            "post_comments": post_comments
        }
        print(post_comments)
        return render(
            request, 
            "blog/single-post.html",
            context
        )

    def post(self, request, slug): 
        """
        Handles the submission of a comment for a specific blog post.

        This method retrieves the blog post identified by the given slug,
        processes the submitted comment form, and saves the comment if valid.
        It also captures the user's IP address and associates it with the comment.

        Args:
            request: The HTTP request object containing the submitted data.
            slug (str): The slug of the blog post to which the comment is being added.

        Returns:
            HttpResponseRedirect: Redirects to the single post page if the comment is successfully saved.
            render: Renders the single post page with the post details and an empty comment form if the form is invalid.
        """
        post = get_object_or_404(Post, slug=slug)
        authenticated = request.user.is_authenticated
        user = request.user
        ip_address = request.META.get('REMOTE_ADDR')
        comment_form = (
            CommentForm(request.POST)
        )
        post_comments = post.post_comments.all().order_by("-created_at")
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.user = user if authenticated else None
            comment.ip_adress = ip_address
            comment.save()
            return HttpResponseRedirect(
                reverse("single-post-page",
                    args=[slug]
                )
            )
        context = {
            "post": post,
            "post_tags": post.tag.all(),
            "comment_form": CommentForm(),
            "post_comments": post_comments
        }
        print(post_comments)
        return render(
            request, 
            "blog/single-post.html",
            context
        )
