from django.shortcuts import render
from .models import Post


def home_view(request):
    posts = Post.objects.all()
    return render(request, "a_posts/home.html", {"posts": posts})

