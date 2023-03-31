
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass

class CustomUserProfile(models.Model):
    custom_user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField()
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
