from django.shortcuts import render
from .models import Post

# Create your views here.


def bloghome(request):
    allPosts = Post.objects.all()
    context = {'allPosts': allPosts}
    return render(request, 'blog/blogHome.html', context)


def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first() # OR [0]
    context = {'post':post}
    return render(request, 'blog/blogPost.html', context)