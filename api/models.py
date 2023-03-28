from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CASCADE


class CustomUser(AbstractUser):    # CustomUserを使用, auth.Userモデルとの衝突がを解消
  pass


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=CASCADE, null=True)
    title = models.CharField(max_length=50)
    body = models.TextField(default='body-data', max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(
        'Category',
        blank=True,
        related_name="tasks",
    )

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=1024)
    slug = models.CharField(max_length=1024, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.name}'
