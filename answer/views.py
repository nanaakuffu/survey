from django.shortcuts import render, redirect
from django.http import HttpResponse

from helpers.functions import is_ajax
from .models import Answer, Question
from django.forms.models import model_to_dict
# from .form import QuestionForm
import json


# Create your views here.
def answers(request):
    answers_data = Answer.objects.order_by('id')
    questions = Question.objects.order_by('id').values('id')
    choices = ['A', 'B', 'C', 'D']
    return render(request, 'index/answers.html', {'answers': answers_data,
                                                  'questions': questions,
                                                  'choices': choices}
                  )


def show(request):
    if is_ajax(request):
        answer_id = request.GET.get('answerID')
        data = model_to_dict(Answer.objects.get(id=answer_id))
    return HttpResponse(json.dumps(data), content_type='application/json')


def update(request):
    answer_id = request.POST.get('id')

    data = Answer.objects.get(id=answer_id)
    data.answer = request.POST.get('answer')
    data.question.id = request.POST.get('question')
    data.choice = request.POST.get('choice')
    data.needs_recommendation = 1 if request.POST.get(
        'needs_recommendation') else 0
    data.save()

    return redirect('answers')


def save(request):
    data = Answer()
    data.answer = request.POST.get('answer')
    data.question = request.POST.get('question')
    data.choice = request.POST.get('choice')
    data.needs_recommendation = 1 if request.POST.get(
        'needs_recommendation') else 0
    data.save()

    return redirect('answers')
