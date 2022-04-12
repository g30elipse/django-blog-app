from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='posts-home'),
    path('posts', views.all_blogs, name='all-posts'),
    path('posts/<str:slug>', views.blog_detail, name='post-detail'),
]
