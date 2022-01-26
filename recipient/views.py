from django.db import DatabaseError
from django.shortcuts import render, redirect
from django.http import HttpResponse
from helpers.functions import is_ajax, response_data
from recipient.models import Recipient
from django.forms.models import model_to_dict


# Create your views here.
def recipients(request) -> HttpResponse:
    if request.method == "GET":
        recipient_data = Recipient.objects.all()
        return render(request, 'index/recipients.html', {'recipients': recipient_data})
    else:
        try:
            data = Recipient()
            data.name = request.POST.get('name')
            data.email = request.POST.get('email')
            data.contact_number = request.POST.get('contact_number')
            data.institution = request.POST.get('institution')

            data.save()
            message = "Request completed successfully."
            status = 200
        except DatabaseError:
            message = "Sorry! An error occured."
            status = 500

        return response_data(message=message, status=status)


def show(request, id) -> HttpResponse:
    data = model_to_dict(Recipient.objects.get(id=id))

    return response_data(data=data, message="Request completed successfully.")


def update(request, id) -> HttpResponse:
    try:
        data = Recipient.objects.get(id=id)
        data.name = request.POST.get('name')
        data.email = request.POST.get('email')
        data.contact_number = request.POST.get('contact_number')
        data.institution = request.POST.get('institution')

        data.save()
        message = "Request completed successfully."
        status = 200
    except DatabaseError:
        message = "Sorry! An error occured."
        status = 500

    return response_data(message=message, status=status)
