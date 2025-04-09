from django.contrib import admin
from .models import Question, Answer, UpVote

# Register your models here.
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'created_at']

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['user', 'question', 'content', 'created_at']

@admin.register(UpVote)
class Upvote(admin.ModelAdmin):
    list_display = ['user', 'answer', 'created_at']