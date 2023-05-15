from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.models import User


# Register your models here.

@admin.register(User)
class UserAdminModel(ModelAdmin):
    list_display = ('id','username','first_name')