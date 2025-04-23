from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.BlogListView.as_view(), name='blog'),
    path('<int:pk>/', views.BlogDetailView.as_view(), name='post_detail'),
]
