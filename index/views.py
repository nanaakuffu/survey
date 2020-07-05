from django.shortcuts import render
from django.db.models import Case, When
from django.http import HttpResponse
from survey.models import Survey
import json

# Create your views here.
def index(request):
    results = Survey.objects.select_related('recipient').only('recipient__name', \
        'recipient__institution', 'hasresponded', 'recipient__survey_link', \
            'date_sent', 'date_responded')
    context = {'results' : results}
    return render(request, 'index/index.html', context)

def home(request):
    if request.is_ajax():
        json_response = {'sent' : Survey.objects.all().count(), 'response' :  Survey.objects.filter(hasresponded=1).count()}
    return HttpResponse(json.dumps(json_response), content_type='application/json')