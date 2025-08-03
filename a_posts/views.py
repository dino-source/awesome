# views.py in Django is a CONTROLLER (see MVC architectural pattern)!!!
# business logic should be in a separate level - services.py !!!


import requests
from bs4 import BeautifulSoup
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Tag
from .forms import PostCreateForm, PostEditForm


def home_view(request, tag=None):
    if tag:
        posts = Post.objects.filter(tags__slug=tag)
        tag = get_object_or_404(Tag, slug=tag)
    else:
        posts = Post.objects.all()

    categories = Tag.objects.all()

    context = {
        "posts": posts,
        "categories": categories,
        "tag": tag,
    }

    return render(request, "a_posts/home.html", context)


def post_create_view(request):
    form = PostCreateForm()
    if request.method == "POST":
        form = PostCreateForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)

            website = requests.get(form.data["url"])
            html_sourcecode = BeautifulSoup(website.text, "html.parser")

            find_image = html_sourcecode.select(
                "meta[content^='https://live.staticflickr.com/']"
            )
            image = find_image[0]["content"]
            post.image = image

            find_title = html_sourcecode.select("h1.photo-title")
            title = find_title[0].text.strip()
            post.title = title

            find_artist = html_sourcecode.select("a.owner-name")
            artist = find_artist[0].text.strip()
            post.artist = artist

            post.author = request.user

            post.save()
            form.save_m2m()
            return redirect("home")

    return render(request, "a_posts/post_create.html", {"form": form})


def post_delete_view(request, pk):
    post = get_object_or_404(Post, id=pk)
    if request.method == "POST":
        post.delete()
        return redirect("home")

    return render(request, "a_posts/post_delete.html", {"post": post})


def post_edit_view(request, pk):
    post = get_object_or_404(Post, id=pk)
    form = PostEditForm(instance=post)

    if request.method == "POST":
        form = PostEditForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Post has been updated")
            return redirect("home")

    context = {
        "post": post,
        "form": form,
    }

    return render(request, "a_posts/post_edit.html", context)


def post_page_view(request, pk):
    post = get_object_or_404(Post, id=pk)
    return render(request, "a_posts/post_page.html", {"post": post})
