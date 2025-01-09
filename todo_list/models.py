from django.db import models
import datetime

# Create your models here.


class TaskList(models.Model):
    # id = models.IntegerField()
    title = models.CharField(unique=True, max_length=200, blank=False)
    assigned_date = models.DateTimeField(auto_now_add=True)
    completed_date = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=True)

    def __str__(self):
        return self.title
