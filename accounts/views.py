from django.db import DatabaseError
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
from .models import CustomUser
from helpers.functions import response_data

# Create your views here.


def get_users(request: HttpRequest) -> HttpResponse:
    users = CustomUser.objects.all()
    return render(request=request, template_name="index/users.html", context={"users": users})


def get_user_profile(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        return render(request=request, template_name="index/profile.html", context={"user": request.user})
    else:
        try:
            user = request.user
            user.email = request.POST.get('email')
            user.first_name = request.POST.get('first_name')
            user.last_name = request.POST.get('last_name')

            user.save()
            status = 200
            message = "Data saved successfully."
        except DatabaseError:
            status = 500
            message = "Sorry! An error ocurred."

        return response_data(status=status, message=message)


def create_user(request: HttpRequest):
    try:
        user = CustomUser()
        user.first_name = request.POST.get("first_name")
        user.last_name = request.POST.get("last_name")
        user.email = request.POST.get("email")
        user.password = make_password(request.POST.get("password"))

        user.save()
        status = 200
        message = "Data saved successfully."
    except DatabaseError:
        status = 500
        message = "Sorry! An error ocurred."

    return response_data(status=status, message=message)
