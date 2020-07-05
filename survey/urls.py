from . import views
from django.urls import path

urlpatterns = [
    path('survey/send_survey', views.send_survey, name='send_survey'),
    path('survey/survey', views.get_questions, name='survey'),
    path('survey/process', views.process_survey, name='process_survey'),
    path('survey/sent', views.sent_page, name='sent'),
    path('survey/analytics', views.get_analytics, name='analytics')
]