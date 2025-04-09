
from django.db import models
from django.contrib.auth import get_user_model
import markdown

User = get_user_model()

class Question(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['title']),
            models.Index(fields=['created_at']),
        ]

    def __str__(self):
        return f"Question by {self.user} on {self.title}"


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, related_name="answers", on_delete=models.CASCADE)
    content = models.TextField()
    likes = models.ManyToManyField(User, related_name="liked_answers", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    votes = models.ManyToManyField(User, related_name='voted', through='UpVote')


    class Meta:
        indexes = [
            models.Index(fields=['content']),
            models.Index(fields=['created_at']),
        ]
        unique_together = ('question', 'user')

    def __str__(self):
        return f"Answer by {self.user} on {self.question}"

    def get_content_as_html(self):
        html_content = markdown.markdown(self.content)
        return f'<div class="answer">{html_content}</div>'

    def has_user_voted(self, user):
        return self.votes.filter(id=user.id).exists()


class UpVote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='votes')
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='ans_votes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'answer')

    def __str__(self):
        return f"Vote by {self.user} on answer {self.answer.id}"
