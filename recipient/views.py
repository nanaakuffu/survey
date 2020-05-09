from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Recipient
from django.forms.models import model_to_dict
from .form import RecipientForm
import json

# Create your views here.
def recipients(request):
    recipients = Recipient.objects.all()
    return render(request, 'index/recipients.html', {'recipients' : recipients})

def show(request):
    if request.is_ajax():
        dataID = request.GET.get('dataID')
        data = model_to_dict(Recipient.objects.get(id=dataID))
    return HttpResponse(json.dumps(data), content_type='application/json')

def update(request):
    id = request.POST.get('key')
    
    data = Recipient.objects.get(id = id)
    data.name = request.POST.get('name')
    data.email = request.POST.get('email')
    data.contact = request.POST.get('contact')
    data.institution = request.POST.get('institution')
    data.save()

    return redirect('recipients')

def save(request):
    data = Recipient()
    data.name = request.POST['name']
    data.email = request.POST['email']
    data.contact = request.POST['contact']
    data.institution = request.POST['institution']
    data.save()

    return redirect('recipients')