from datetime import date
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.


def home(request):
    recent_blogs = Post.objects.all().order_by('-date')[:3]
    return render(request, 'blog/home.html', {'blogs': recent_blogs})


def all_blogs(request):
    blogs = Post.objects.all().order_by('-date')
    return render(request, 'blog/blogs.html', {'blogs': blogs})


def blog_detail(request, slug):
    blog = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/blog.html', {
        'blog': blog,
        'tags': blog.tags.all()
    })
