from datetime import date
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.


class BlogListView(ListView):
    template_name = 'blog/blogs.html'
    context_object_name = 'blogs'
    model = Post
    ordering = '-date'


class BlogDetailView(DetailView):
    template_name = 'blog/blog.html'
    context_object_name = 'blog'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = self.object.tags.all()
        return context


class HomeView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'blogs'
    ordering = ['-date']
    paginate_by = 3
