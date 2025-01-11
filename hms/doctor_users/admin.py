from django.contrib import admin
from .models import ScheduleTime
# Register your models here.


# @admin.register(ScheduleTime)
# class Schedule(admin.ModelAdmin):
#     lst = ['deptId', 'userId']

admin.site.register(ScheduleTime)