
from django.urls import path

from app import views


urlpatterns = [
    path('index/', views.index, name='index'),
    path('about/', views.about, name='index'),
    path('info/<int:id>', views.info, name ='info'),
    path('list/', views.list, name='list'),
]