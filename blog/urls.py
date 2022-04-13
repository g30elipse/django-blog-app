from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('blogs', views.all_blogs, name='all-blogs'),
    path('blogs/<str:slug>', views.blog_detail, name='blog-detail'),
]
