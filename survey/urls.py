from . import views
from django.urls import path

urlpatterns = [
    path('survey/send-survey', views.send_survey, name='send_survey'),
    path('survey', views.get_questions, name='survey'),
    path('survey/process', views.process_survey, name='process_survey'),
    path('survey/sent', views.sent_page, name='sent'),
    path('survey/analytics/data', views.get_analytics, name='analytics'),
    path('survey/analytics', views.analytics_page, name='analytics_page')
]
