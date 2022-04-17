from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='blog-home'),
    path('blogs', views.BlogListView.as_view(), name='all-blogs'),
    path('blogs/<str:slug>', views.BlogDetailView.as_view(), name='blog-detail'),
]
