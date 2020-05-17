from . import views
from django.urls import path

urlpatterns = [
    path('research/send_survey', views.send_survey, name='send_survey'),
    path('research/survey', views.get_questions, name='survey'),
    path('research/process', views.process_survey, name='process_survey'),
    # path('recipients/save', views.save, name='saverecipient' )
]