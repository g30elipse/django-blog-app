from datetime import date
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView
from django.views import View
from .models import Post
from .forms import CommentForm

# Create your views here.


class BlogListView(ListView):
    template_name = 'blog/blogs.html'
    context_object_name = 'blogs'
    model = Post
    ordering = '-date'


class BlogDetailView(View):
    template_name = 'blog/blog.html'

    def get(self, request, slug):
        blog = get_object_or_404(Post, slug=slug)
        form = CommentForm()
        return render(request, self.template_name, {
            'blog': blog,
            "tags": blog.tags.all(),
            "comment_form": form,
            "comments": blog.comments.all().order_by('-id')
        })

    def post(self, request, slug):
        blog = get_object_or_404(Post, slug=slug)
        comment = CommentForm(request.POST)
        comment.instance.post = blog
        if comment.is_valid():
            comment.save()
            return redirect(reverse('blog-detail', kwargs={'slug': slug}))

        return render(request, self.template_name, {
            'blog': blog,
            "tags": blog.tags.all(),
            "comment_form": comment,
            "comments": blog.comments.all().order_by('-id')
        })


class HomeView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'blogs'
    ordering = ['-date']
    paginate_by = 3
