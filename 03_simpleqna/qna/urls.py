from django.urls import path
from .views import QuestionListView, QuestionDetailView, AskQuestionView, UpVoteView

urlpatterns = [
    path('questions/', QuestionListView.as_view(), name='question_details'),
    path('questions/<int:pk>/', QuestionDetailView.as_view(), name='question_detail'),
    path('ask-question/', AskQuestionView.as_view(), name='ask_question'),
    path('answers/<int:answer_id>/vote/', UpVoteView.as_view(), name='vote_answer'),
]
