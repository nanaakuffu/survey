from django.shortcuts import render, redirect
from django.http import HttpResponse

from helpers.functions import is_ajax
from .models import Question
from django.forms.models import model_to_dict
from .form import QuestionForm
import json


# Create your views here.
def questions(request):
    questions_data = Question.objects.order_by('id')
    return render(request, 'index/questions.html', {'questions': questions_data})


def show(request):
    if is_ajax(request):
        question_id = request.GET.get('questionID')
        data = model_to_dict(Question.objects.get(id=question_id))
    return HttpResponse(json.dumps(data), content_type='application/json')


def update(request):
    question_id = request.POST.get('key')

    data = Question.objects.get(id=question_id)
    data.question_text = request.POST.get('question_text')
    data.recommendation = request.POST.get('recommendation')
    data.save()

    return redirect('questions')


def save(request):
    data = Question()
    data.question_text = request.POST.get('question_text')
    data.recommendation = request.POST.get('recommendation')
    data.save()

    return redirect('questions')
