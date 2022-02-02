# Django related modules
from email import message
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms.models import model_to_dict
from django.template import RequestContext

from helpers.functions import hash_string, is_ajax, response_data
from .models import Answer, Question, Survey, Response, Recipient
from survey.models import QuestionsAndAnswers, Analytics
from django.conf import settings
from django.core.mail import EmailMessage
from django.db.models import Count
from django.core import serializers

from helpers.printing import PDF

from random import randint
from datetime import date
import json

SUCCESS_MESSAGE = "Request completed successfully."

# Create your views here.


def send_survey(request):
    recipient = Recipient.objects.get(id=request.POST.get('id'))

    recipient_id = recipient.id
    recipient_email = [recipient.email]
    survey_id = str(randint(1000000, 9999999))
    sender = settings.EMAIL_HOST_USER
    link_prefix = request.scheme+"://"+request.get_host()

    survey_link = f'{link_prefix}/survey?id={recipient_id}&sid={survey_id}&mid={recipient_email[0]}'

    email_message = "<p> Dear Sir/Madam, </p> \
                        <p> PharmAccess Ghana welcomes you to its self-administered basic quality assessment tool. </p> \
                        <p> We invite you to take this quick (15 minutes) survey about your health facility to objectively evaluate some basic quality issues by clicking on the link below </p> \
                        <p>" + survey_link + "</p>"
    subject = "MyBQualityScan Survey"

    message_email = EmailMessage(
        subject=subject,
        body=email_message,
        from_email=sender,
        to=recipient_email
    )
    message_email.content_subtype = 'html'

    # Check if the recipient has already been served a survey
    if Survey.objects.filter(recipient=recipient_id).count() == 0:
        # If no try sending the survey but if not report double
        if message_email.send():
            # Save the link in the recipient table
            recipient.survey_link = survey_link
            recipient.save()

            # Save the details in the survey table
            survey = Survey()
            survey.recipient = recipient
            survey.date_sent = date.today()
            survey.hasresponded = 0
            survey.survey_id = int(survey_id)
            survey.save()

            # Send the response to the  ajax and then to template
            status = 200
            message = SUCCESS_MESSAGE
        else:
            # Sending was unsuccessful. Report on that
            status = 500
            message = "Sorry an occured while sending the survey. Please try again."
    else:
        status = 400
        message = "This recipient has already been served."

    return response_data(status=status, message=message)


def get_questions(request):
    if request.method == 'GET':
        # Get the questions and answers from the db view
        # The answers portion of QuestionsAndAnswers is a json data
        survey_questions = QuestionsAndAnswers.objects.all().only('question_text', 'answers')

        # Get the variables that came with the url and the associated data
        survey_id = request.GET.get('sid')
        survey = Survey.objects.get(survey_id=survey_id)
        e_mail = request.GET.get('mid')
        recipient_id = request.GET.get('id')
        # If 1 then recipient exist else no
        recipient_exists = Recipient.objects.filter(id=recipient_id).count()

        # Set the date for the survey
        survey_date = date.today()

        # Create the context for the template
        context = {
            'survey_form': survey_questions,
            'recipient': recipient_id,
            'email': e_mail,
            'survey': survey_id,
            'survey_date': survey_date,
            'has_responded': survey.hasresponded,
            'recipient_exists': recipient_exists
        }

        # Send info to the template
        return render(request, "index/survey.html", context=context)


def process_survey(request):
    r_id = request.POST.get('recipient_id')
    s_id = request.POST.get('survey_id')
    random_file_name = hash_string(20)

    exception_list = ['survey_id', 'recipient_id',
                      'survey_date', 'email', 'csrfmiddlewaretoken']

    # Get the recipient and survey corresponding data
    recipient = Recipient.objects.get(id=r_id)
    survey = Survey.objects.get(survey_id=s_id)
    counter = 1

    # Get the data that needs recommendation and that would be put on the pdf
    headers = {'name': recipient.name,
               'facility': recipient.institution,
               'date': request.POST.get('survey_date')
               }

    needs_recommendation = {}
    for key, value in request.POST.items():
        if key not in exception_list:
            question = Question.objects.get(id=key)
            answer = Answer.objects.get(id=value)
            if answer.needs_recommendation == 1:
                needs_recommendation[counter] = [
                    question.question_text,
                    answer.answer,
                    question.recommendation
                ]
                counter += 1

    file_name = f'./static/survey/files/{random_file_name}.pdf'

    # Print those which needs recommendation to pdf
    report = PDF(file_name, 'A4')
    is_pdf_created = report.make_pdf(headers, needs_recommendation)

    if is_pdf_created:
        # Send a mail to the person who filled the survey with an attachment
        survey_subject = "MyBQualityScan"
        survey_message = "<p> Dear Sir/Madam, </p> \
                        <p> Kindly find attached a detailed recommendation based on your answers to the questions in the survey.</p> \
                        <p> Please carefully peruse this document and where necessary apply the suggested recommendations.</p> \
                        <br /> \
                        <p> Regards,</p>"

        survey_from = settings.EMAIL_HOST_USER
        survey_to = [request.POST.get('email')]

        survey_email = EmailMessage(subject=survey_subject,
                                    body=survey_message,
                                    from_email=survey_from,
                                    to=survey_to)
        survey_email.attach_file(file_name)
        survey_email.content_subtype = "html"

        survey_email.send(fail_silently=False)

        # Save the results from the form to the database
        for key, value in request.POST.items():
            responses = Response()
            if key not in exception_list:
                answer = Answer.objects.get(id=value)
                responses.question = Question.objects.get(id=key)
                responses.answer = answer
                responses.recipient = recipient
                responses.survey = survey
                responses.choice = answer.choice
                responses.save()

        # Update the survey details by adding the pdf filename and indicating that respondent has responded.
        survey.hasresponded = 1
        survey.date_responded = date.today()
        survey.file_name = file_name.split('/')[-1]
        survey.save()

        status = 200
        message = "Request completed successfully"
    else:
        status = 400
        message = "Mail Sending Error"

    return response_data(status=status, message=message)


def sent_page(request):
    return render(request, 'index/sent_page.html')


def get_analytics(request):
    query = Analytics.objects.all().values()
    data = [item for item in query]

    return response_data(data=data, status=200, message="Request completed successfully.")


def analytics_page(request):
    query = Analytics.objects.all()

    context = {'analytics': query}
    return render(request, "index/analytics.html", context=context)
