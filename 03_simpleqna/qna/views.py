
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views import View
from django.views.decorators.cache import cache_control

from .models import Question, Answer, UpVote
from .forms import QuestionForm, AnswerForm
from django.utils.decorators import method_decorator
from django.http import JsonResponse, HttpResponseForbidden


class QuestionListView(View):
    def get(self, request):
        username = request.user.username
        questions = Question.objects.all().order_by('-created_at')
        return render(request, 'home/questions.html', {'questions': questions, 'username':username})


@method_decorator(
    [login_required(login_url='login'), cache_control(no_cache=True, no_store=True, must_revalidate=True)],
    name='dispatch'
)
class QuestionDetailView(View):
    def get(self, request, pk):
        question = get_object_or_404(Question, pk=pk)
        form = AnswerForm()
        username = request.user.username
        user_answer = Answer.objects.filter(question=question, user=request.user).first()
        if user_answer:
            form = AnswerForm(instance=user_answer)

        return render(request, 'home/question_detail.html', {
            'question': question,
            'form': form,
            'username': username
        })

    def post(self, request, pk):
        question = get_object_or_404(Question, pk=pk)
        user_answer = Answer.objects.filter(question=question, user=request.user).first()
        username = request.user.username
        if question.user == request.user:
            return HttpResponseForbidden("You can't answer your own question.")

        if user_answer:
            form = AnswerForm(request.POST, instance=user_answer)
        else:
            form = AnswerForm(request.POST)

        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.question = question
            answer.save()
            return redirect('question_detail', pk=pk)

        return render(request, 'home/question_detail.html', {
            'question': question,
            'form': form,
            'username': username
        })


@method_decorator([login_required(login_url='login'), cache_control(no_cache=True, no_store=True, must_revalidate=True)],
    name='dispatch'
)
class AskQuestionView(View):
    def get(self, request):
        form = QuestionForm()
        username = request.user.username
        return render(request, 'home/ask_question.html', {'form': form, 'username': username})

    def post(self, request):
        username = request.user.username
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            return redirect('question_details')
        return render(request, 'home/ask_question.html', {'form': form, 'username': username})


@method_decorator(login_required(login_url='login'), name='dispatch')
class UpVoteView(View):
    def post(self, request, answer_id):
        answer = get_object_or_404(Answer, id=answer_id)
        user = request.user

        existing_vote = UpVote.objects.filter(user=user, answer=answer).first()

        if existing_vote:
            existing_vote.delete()
            voted = False
        else:
            UpVote.objects.create(user=user, answer=answer)
            voted = True

        total_votes = UpVote.objects.filter(answer=answer).count()

        return JsonResponse({
            'voted': voted,
            'total_votes': total_votes
        })
