from django.db import models
from django.contrib.auth.models import User
from django.templatetags.static import static


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="avatars/", null=True, blank=True)
    realname = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(unique=True, null=True)
    location = models.CharField(max_length=20, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)

    @property
    def avatar(self):
        avatar = static("images/avatar_default.svg")
        if self.image and self.image.url:
            avatar = self.image.url
        return avatar

    @property
    def is_avatar_set(self):
        return self.image and self.image.url

    @property
    def name(self):
        if self.realname:
            name = self.realname
        else:
            name = self.user.username
        return name
