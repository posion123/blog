
from django.urls import path

from app import views


urlpatterns = [
    path('index/', views.index, name='index'),
    path('about/', views.about, name='index'),
    path('info/<int:id>', views.info, name ='info'),
    path('list/', views.list, name='list'),
    path('my_list/<int:id>/', views.my_list, name='my_list'),
    path('all_photoes/', views.all_photoes, name='all_photoes'),
    path('person_photoes/<int:id>/', views.person_photoes, name='person_photoes'),
    path('search/', views.search, name='search'),
    path('message/', views.message, name='message'),
]
