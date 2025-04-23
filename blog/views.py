from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from .models import Post


class BlogListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog.html'
    login_url = 'login'  # Redirects to this URL if not authenticated


class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'post.html'
    login_url = 'login'
