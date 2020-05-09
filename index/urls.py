from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    # path('recipients', views.recipients, name='recipients'),
    # path('home', views.home, name='home'),
    # path('showdata', views.showData, name='show'),
    # path('updatedata', views.updateData, name='update')
    # path('', views.PostDetail.as_view(), name='post_detail'),
]