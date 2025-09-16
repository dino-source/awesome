from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import get_object_or_404

from a_core.utils import maybe_unused
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    maybe_unused(kwargs, sender)
    user = instance
    if created:
        Profile.objects.create(
            user=user,
            email=user.email,
        )
    else:
        profile = get_object_or_404(Profile, user=user)
        profile.email = user.email
        profile.save()


@receiver(post_save, sender=Profile)
def update_user(sender, instance, created, **kwargs):
    maybe_unused(kwargs, sender)
    profile = instance
    if not created:
        user = get_object_or_404(User, id=profile.user.id)
        if user.email != profile.email:
            user.email = profile.email
            user.save()
