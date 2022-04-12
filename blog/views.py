from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'blog/home.html')


def all_blogs(request):
    return render(request, 'blog/blogs.html')


def blog_detail(request, slug):
    return render(request, 'blog/blog.html', {'slug': slug})
