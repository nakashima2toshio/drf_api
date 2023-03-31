from django.db import models
from django.contrib.auth.models import AbstractUser

from sns_app.models import Post


class CustomUser(AbstractUser):
    pass

