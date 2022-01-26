from . import views
from django.urls import path

urlpatterns = [
    path('users', views.get_users, name='users'),
    path('profile', views.get_user_profile, name='profile'),
    path('user', views.create_user, name='user'),
]
