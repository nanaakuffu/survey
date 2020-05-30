# Django related modules
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms.models import model_to_dict
from .models import Answer, Question, Survey, Response, Recipient, QuestionsAndAnswers
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMessage

from research.printing import PDF
from io import BytesIO

# Non django related modules
from matplotlib.pyplot import plot as plt
import pandas as pd
import seaborn as sns; sns.set()
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

        # Check if the recipient has already been served a survey
        if Survey.objects.filter(recipient=iD).count() == 0: 
            # If no try sending the survey but if not report double
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
                data = {'status': 'failure'}
        else:
            data = {'status': 'double'}

    return HttpResponse(json.dumps(data), content_type='application/json')


def get_questions(request):
    if request.method == 'GET':
        # Get the questions and anwers from the db view
        # The answers portion of QuestionsAndAnswers is a json data
        surveyQuestions = QuestionsAndAnswers.objects.all().only('question_text', 'answers')

        # Get the variables that came with the url and the associated data
        surveyID = request.GET.get('sid')
        survey = Survey.objects.get(survey_id = surveyID)
        eMail = request.GET.get('mid')
        recipientID = request.GET.get('id')
        recipients = Recipient.objects.filter(id = recipientID).count()
        
        # Set the date for the durvey
        surveyDate = date.today()

        # Create the context for the template
        context = { 'survey_form' : surveyQuestions, 'recipient' : recipientID, 
                    'email': eMail, 'survey' : surveyID, 'survey_date' : surveyDate,
                    'hasResponded' : survey.hasresponded, 'recipientExists' : recipients }

        # Send info to the template
        return render(request, "index/survey.html", context=context)


def process_survey(request):
    if request.is_ajax():
        rID = request.POST.get('recipient_id')
        sID = request.POST.get('survey_id')

        exceptionList = ['survey_id', 'recipient_id', 'survey_date', 'email', 'csrfmiddlewaretoken']

        # Get the recipient and survey corresponding data
        recipient = Recipient.objects.get(id=rID)
        survey = Survey.objects.get(survey_id=sID)
        counter = 1

        # Get the answers that needs recommendation
        needsRecommendation = {}
        for key, value in request.POST.items():
            tmpList = []
            if key not in exceptionList:
                question = Question.objects.get(id=key)
                answer = Answer.objects.get(id=value)
                if answer.needs_recommendation == 1:
                    tmpList.append(question.question_text)
                    tmpList.append(answer.answer)
                    tmpList.append(question.recommendation)
                    needsRecommendation[counter] = tmpList
                    counter += 1

        fileName = './static/survey/files/' + '_'.join(str(recipient.institution).split()) + '.pdf'

        # Print those which needs recommendation to pdf
        report = PDF(fileName, 'A4')
        isPDFCreated = report.makePDF(needsRecommendation)

        if isPDFCreated:
            # Send a mail to the person who filled the survey with an attachment
            surveySubject = "MyBQualityScan"
            surveyMessage = "<p> Dear Sir/Madam, </p> \
                            <p> Kindly find attached a detailed recommendation based on your answers to the questions in the survey.</p> \
                            <p> Please carefully peruse this document and where necessary apply the suggested recommendations.</p> \
                            <br /> \
                            <p> Regards,</p>"

            surveyFrom = settings.EMAIL_HOST_USER
            surveyTo = [request.POST.get('email')]

            surveyEmail = EmailMessage(subject=surveySubject, 
                                       body=surveyMessage, 
                                       from_email=surveyFrom, 
                                       to=surveyTo)
            surveyEmail.attach_file(fileName)
            surveyEmail.content_subtype = "html"

            surveyEmail.send(fail_silently=False)

            # Save the results from the form to the database
            for key, value in request.POST.items():
                responses = Response()
                if key not in exceptionList:
                    responses.question = Question.objects.get(id=key)
                    responses.answer = Answer.objects.get(id=value)
                    responses.recipient = recipient
                    responses.survey = survey
                    responses.save()

            # Update the survey details by adding the pdf filename and indicating that respondent has responded.
            survey.hasresponded = 1
            survey.date_responded = date.today()
            survey.file_name = fileName.split('/')[-1]
            survey.save()

            data = {'status': 200 }
        else:
            data = {'status' : 400, "message" : "Mail Sending Error"}
    
    return HttpResponse(json.dumps(data), content_type='application/json')


def sent_page(request):
    return render(request, 'index/sent_page.html')