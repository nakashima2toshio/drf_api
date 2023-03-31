from django.contrib import admin
from api.models import CustomUser, CustomUserProfile

admin.site.register(CustomUser)
admin.site.register(CustomUserProfile)
