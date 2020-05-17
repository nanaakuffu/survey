from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms.models import model_to_dict
from .models import Answer, Question, Survey, Response, Recipient, QuestionsAndAnswers
from django.conf import settings
from django.core.mail import send_mail
from random import randint
from datetime import date
import json

# Create your views here.
def send_survey(request):
    if request.is_ajax():
        iD = request.POST.get('sendID')
        recipient = request.POST.get('sendeMail')
        sID = str(randint(1000000, 9999999))
        sender = settings.EMAIL_HOST_USER
        survey_link = "http://localhost:8000/research/survey?id="+iD+"&sid="+sID+"&mid="+recipient

        email_message = "<p> Dear Sir/Madam, </p> \
                   <p> PharmAccess Ghana welcomes you to its self-administered basic quality assessment tool. </p> \
                   <p> We invite you to take this quick (15 minutes) survey about your health facility to objectively evaluate some basic quality issues by clicking on the link below </p> \
                   <p>"+survey_link+"</p>"
        subject = "MyBQualityScan Survey"

        if send_mail(subject=subject, message=email_message, from_email=sender, recipient_list=[recipient], html_message=email_message):
            # Svae the link in the recipient table
            recipientObj = Recipient.objects.get(id=iD)
            recipientObj.survey_link = survey_link
            recipientObj.save()

            # Save the details in the survey table
            survey = Survey()
            survey.recipient = recipientObj
            survey.date_sent = date.today()
            survey.hasresponded = 0
            survey.survey_id = sID
            survey.save()

            # Send the response to the  ajax and then to template
            data = {'status': 'success'}
        else:
            # Sending was unsuccesfull. Report on that
            data = {'status': 'unsuccessfull'}

    return HttpResponse(json.dumps(data), content_type='application/json')


def get_questions(request):
    survey_form = QuestionsAndAnswers.objects.all().only('question_text', 'answers')
    surveyID = request.GET.get('sid')
    survey = Survey.objects.get(survey_id = surveyID)
    eMail = request.GET.get('mid')
    recipientID = request.GET.get('id')
    recipients = Recipient.objects.filter(id = recipientID).count()
    surveyDate = date.today()
    context = {'survey_form' : survey_form, 'recipient' : recipientID, 
                'email': eMail, 'survey' : surveyID, 'survey_date' : surveyDate,
                'hasResponded' : survey.hasresponded, 'recipientExists' : recipients }
    return render(request, "index/survey.html", context=context)


def process_survey(request):
    pass
    