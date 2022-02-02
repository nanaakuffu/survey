from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Case, When
from django.http import FileResponse, HttpResponse
from helpers.functions import is_ajax, response_data
from survey.models import Survey
import json
import os


# Create your views here.
@login_required
def index(request):
    results = Survey.objects.select_related('recipient').only('recipient__name',
                                                              'recipient__institution',
                                                              'hasresponded',
                                                              'recipient__survey_link',
                                                              'date_sent',
                                                              'date_responded',
                                                              'file_name')
    context = {'results': results}
    return render(request, 'index/index.html', context)


def home(request):
    json_response = {
        "sent": Survey.objects.all().count(),
        "response": Survey.objects.filter(hasresponded=1).count()
    }

    return HttpResponse(json.dumps(json_response), content_type='application/json')


def get_pdf_file(request, file_name):
    __file_string = f"static/survey/files/{file_name}.pdf"

    if os.path.isfile(__file_string):
        __pdf_file = open(f"static/survey/files/{file_name}.pdf", 'rb')

        return FileResponse(__pdf_file)
    else:
        status = 404
        message = "File does not exist"

        return response_data(status=status, message=message)


def get_image(request, img_name):
    __image_file = open(f"static/survey/img/{img_name}.jpg", 'rb')

    return FileResponse(__image_file)
