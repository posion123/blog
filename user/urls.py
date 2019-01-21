from django.urls import path

from user import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('index/', views.index, name='index'),
    path('logout/', views.logout, name='logout'),
    path('all_index/', views.all_index, name='all_index')

]

