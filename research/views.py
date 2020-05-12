from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms.models import model_to_dict
from .models import Answer, Question
from django.conf import settings
from django.core.mail import send_mail
from random import randint
import json

# Create your views here.
def send_survey(request):
    if request.is_ajax():
        
        iD = str(request.POST.get('sendID'))
        recipient = str(request.POST.get('sendeMail'))
        # data = {'id' : iD, 'mail' : recipient}
        sID = str(randint(1000, 9999))
        sender = settings.EMAIL_HOST_USER
        survey_link = "http://localhost:8000/research?id="+iD+"&sid="+sID+"&mid="+recipient
        # data = {'id' : iD, 'mail' : recipient, 'link': survey_link}
        email_message = "<p> Dear Sir/Madam, </p> \
                   <p> PharmAccess Ghana welcomes you to its self-administered basic quality assessment tool. </p> \
                   <p> We invite you to take this quick (15 minutes) survey about your health facility to objectively evaluate some basic quality issues by clicking on the link below </p> \
                   <p>"+survey_link+"</p>"
        subject = "MyBQualityScan Survey"

        # data = {'id' : iD, 'mail' : recipient, 'link': email_message}

        if send_mail(subject=subject, message=email_message, from_email=sender, recipient_list=['nanaakuffu@gmail.com'], html_message=email_message):
            data = {'status': 'success'}
        else:
            data = {'status': 'unsuccessfull'}

    return HttpResponse(json.dumps(data), content_type='application/json')


def get_questions(request):
    # qIDs = Question.objects.values('id')
    # questions_keys = ['question', 'A', 'B', 'C', 'D']
    # d = {}
    # for id in qIDs:
    #     sIDs = Answer.objects.get(question.id = id).values('id', 'question').order_by('choice')
    pass