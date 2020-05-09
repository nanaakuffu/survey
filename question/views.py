from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Question
from django.forms.models import model_to_dict
from .form import QuestionForm
import json

# Create your views here.
def questions(request):
    questions = Question.objects.order_by('id')
    return render(request, 'index/questions.html', {'questions' : questions})

def show(request):
    if request.is_ajax():
        id = request.GET.get('questionID')
        data = model_to_dict(Question.objects.get(id=id))
    return HttpResponse(json.dumps(data), content_type='application/json')

def update(request):
    id = request.POST.get('key')
    
    data = Question.objects.get(id = id)
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