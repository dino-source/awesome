import requests
from bs4 import BeautifulSoup
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Post
from .forms import PostCreateForm, PostEditForm


def home_view(request):
    posts = Post.objects.all()  # type: ignore
    return render(request, "a_posts/home.html", {"posts": posts})


def post_create_view(request):
    form = PostCreateForm()
    if request.method == "POST":
        form = PostCreateForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)

            website = requests.get(form.data["url"])  # type: ignore
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

            post.save()
            return redirect("home")

    return render(request, "a_posts/post_create.html", {"form": form})


def post_delete_view(request, pk):
    post = Post.objects.get(id=pk)  # type: ignore
    if request.method == "POST":
        post.delete()
        return redirect("home")

    return render(request, "a_posts/post_delete.html", {"post": post})


def post_edit_view(request, pk):
    post = Post.objects.get(id=pk)  # type: ignore
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

