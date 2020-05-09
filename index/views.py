from django.shortcuts import render

# Create your views here.
def index(request):
    # results = Survey.objects.select_related('recipient').only('recipient__name', 'recipient__institution', 'hasresponded', 'recipient__survey_link', 'file_name')
    # context = {'results' : results}
    return render(request, 'index/index.html')

def home(request):
    # if request.is_ajax():
    #     json_response = {'sent' : Survey.objects.all().count(), 'response' :  Survey.objects.filter(hasresponded=1).count()}
    #     return HttpResponse(json.dumps(json_response), content_type='application/json')
    pass
