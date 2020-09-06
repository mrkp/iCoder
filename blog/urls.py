# Blog App Urls File

from django.urls import path
from . import views


urlpatterns = [
    path('', views.bloghome, name='bloghome'),
    path('<str:slug>', views.blogPost, name='blogPost'),
]
