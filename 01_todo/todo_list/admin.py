from django.contrib import admin
from .models import TaskList
# Register your models here.


@admin.register(TaskList)
class Task(admin.ModelAdmin):
    list_display = ['title', 'assigned_date', 'completed_date', 'completed']