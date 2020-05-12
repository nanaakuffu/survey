from . import views
from django.urls import path

urlpatterns = [
    path('research/send_survey', views.send_survey, name='send_survey'),
    # path('recipients/show', views.show, name='showrecipient'),
    # path('recipients/update', views.update, name='updaterecipient'),
    # path('recipients/save', views.save, name='saverecipient' )
]