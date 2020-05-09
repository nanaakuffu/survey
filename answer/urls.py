from . import views
from django.urls import path

urlpatterns = [
    path('answers', views.answers, name='answers'),
    path('answers/show', views.show, name='showanswer'),
    path('answers/update', views.update, name='updateanswer'),
    path('answers/save', views.save, name='saveanswer')
]