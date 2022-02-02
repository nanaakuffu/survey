from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('home/<file_name>/pdf', views.get_pdf_file, name='pdf_file'),
    path('home/<img_name>/img', views.get_image, name='image'),
]
