from django.contrib import admin
from .models import UserAuthentication
# Register your models here.

@admin.register(UserAuthentication)
class UserAdminModel(admin.ModelAdmin):
    list_display = ['username','first_name', 'last_name', 'email']
