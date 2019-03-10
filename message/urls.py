from django.urls import path

from message import views

urlpatterns = [
    path('message/', views.message, name='message'),
    path('answer/<int:id>/', views.answer, name='answer'),
    path('del_message/<int:id>/', views.del_message, name='del_message')
]