from . import views
from django.urls import path

urlpatterns = [
    path('questions', views.questions, name='questions'),
    path('questions/show', views.show, name='showquestion'),
    path('questions/update', views.update, name='updatequestion'),
    path('questions/save', views.save, name='savequestion' )
]