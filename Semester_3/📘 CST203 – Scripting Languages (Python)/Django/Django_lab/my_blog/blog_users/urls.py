from django.urls import path
from . import views

urlpatterns = [
    path('blog-users/', views.blog_users, name='blog-users'),
    path('all-users/', views.members, name='all-users'),
]