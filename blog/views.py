from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from .models import Post


class BlogListView(LoginRequiredMixin, ListView):
    """
    Displays a list of all blog posts.

    Inherits from Django's ListView and requires the user to be logged in
    via LoginRequiredMixin.

    :ivar model: The model used for the list view (Post).
    :vartype model: Model
    :ivar template_name: The path to the HTML template used to render the list view.
    :vartype template_name: str
    :ivar login_url: The URL to redirect to if the user is not authenticated.
    :vartype login_url: str
    """
    model = Post
    template_name = 'blog.html'
    login_url = 'login'  # Redirects to this URL if not authenticated


class BlogDetailView(LoginRequiredMixin, DetailView):
    """
    Displays the details of a single blog post.

    Inherits from Django's DetailView and requires the user to be logged in
    via LoginRequiredMixin.

    :ivar model: The model used for the detail view (Post).
    :vartype model: Model
    :ivar template_name: The path to the HTML template used to render the detail view.
    :vartype template_name: str
    :ivar login_url: The URL to redirect to if the user is not authenticated.
    :vartype login_url: str
    """
    model = Post
    template_name = 'post.html'
    login_url = 'login'
