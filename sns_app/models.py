#
from django.db import models
# from api.models import CustomUser


class Profile(models.Model):
    custom_user = models.OneToOneField('api.CustomUser', on_delete=models.CASCADE)
    display_name = models.CharField(max_length=50)
    bio = models.TextField(blank=True)


class Post(models.Model):
    custom_user = models.ForeignKey('api.CustomUser', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    custom_user = models.ForeignKey('api.CustomUser', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    custom_user = models.ForeignKey('api.CustomUser', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Follow(models.Model):
    follower = models.ForeignKey('api.CustomUser', related_name='following', on_delete=models.CASCADE)
    followed = models.ForeignKey('api.CustomUser', related_name='followers', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
