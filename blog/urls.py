from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blogs-home'),
    path('<str:slug>', views.blog, name='blogs-blog'),
]
