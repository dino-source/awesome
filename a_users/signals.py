from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import get_object_or_404
from .models import Profile


def intentionally_unused_params(sender, **kwargs):
    # The purpose of this method is just to make Pyright happy
    # To force to stop it complaining about unused parameters
    if kwargs and sender:
        pass


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    intentionally_unused_params(sender, **kwargs)
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
    intentionally_unused_params(sender, **kwargs)
    profile = instance
    if not created:
        user = get_object_or_404(User, id=profile.user.id)
        if user.email != profile.email:
            user.email = profile.email
            user.save()
