import requests
from bs4 import BeautifulSoup
from django import forms
from django.forms.models import ModelForm
from django.shortcuts import render, redirect
from .models import Post


def home_view(request):
    posts = Post.objects.all()  # type: ignore
    return render(request, "a_posts/home.html", {"posts": posts})


class PostCreateForm(ModelForm):
    class Meta:
        model = Post
        fields = ["url", "body"]
        labels = {
            "body": "Caption",
        }
        widgets = {
            "body": forms.Textarea(
                attrs={
                    "rows": 3,
                    "placeholder": "Add a caption...",
                    "class": "font1 text-4xl",
                }
            ),
            "url": forms.TextInput(
                attrs={
                    "placeholder": "Add url...",
                }
            ),
        }


def post_create_view(request):
    form = PostCreateForm()
    if request.method == "POST":
        form = PostCreateForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)

            website = requests.get(form.data["url"])
            html_sourcecode = BeautifulSoup(website.text, "html.parser")

            find_image = html_sourcecode.select("meta[content^='https://live.staticflickr.com/']")
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
    post = Post.objects.get(id=pk)
    if request.method == "POST":
        post.delete()
        return redirect("home")

    return render(request, "a_posts/post_delete.html", {"post": post})

