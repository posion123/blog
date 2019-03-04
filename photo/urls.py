from django.urls import path
from photo import views

urlpatterns = [
    path('photoes/', views.photoes, name='photoes'),
    path('add_photoes/', views.add_photoes, name='add_photoes'),
    path('del_photoes/<int:id>/', views.del_photoes, name='del_photoes'),
    path('up_photoes/<int:id>/', views.up_photoes, name='up_photoes'),
    path('my_file/', views.my_file, name='my_file'),
    path('test/', views.test, name='test')
]