from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('home/<file_name>', views.get_pdf_file, name='pdf_file'),
]
