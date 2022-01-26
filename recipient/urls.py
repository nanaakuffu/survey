from . import views
from django.urls import path

urlpatterns = [
    path('recipients', views.recipients, name='recipients'),
    path('recipients/<int:id>/edit', views.show, name='showrecipient'),
    path('recipients/<int:id>/update', views.update, name='updaterecipient'),
]
