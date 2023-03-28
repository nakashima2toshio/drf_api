from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Category
from .models import CustomUser
# Register your models here.
from .models import Task

admin.site.register(Task)
admin.site.register(Category)
admin.site.register(CustomUser, UserAdmin)