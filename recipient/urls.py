from . import views
from django.urls import path

urlpatterns = [
    path('recipients', views.recipients, name='recipients'),
    path('recipients/show', views.show, name='showrecipient'),
    path('recipients/update', views.update, name='updaterecipient'),
    path('recipients/save', views.save, name='saverecipient' )
]