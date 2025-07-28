from django.shortcuts import render
from .forms import ProfileForm


def profile_view(request):
    profile = request.user.profile
    return render(request, "a_users/profile.html", {"profile": profile})


def profile_edit_view(request):
    form = ProfileForm(instance=request.user.profile)
    return render(request, "a_users/profile_edit.html", {"form": form})
