from django.shortcuts import render
from django.http import HttpResponse
from django.forms.models import model_to_dict
from .models import Answer, Question

# Create your views here.
def get_questions(request):
    qIDs = Question.objects.values('id')
    questions_keys = ['question', 'A', 'B', 'C', 'D']
    d = {}
    for id in qIDs:
        sIDs = Answer.objects.get(question.id = id).values('id', 'question').order_by('choice')