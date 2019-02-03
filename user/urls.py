from django.urls import path

from user import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('index/', views.index, name='index'),
    path('logout/', views.logout, name='logout'),
    path('all_index/', views.all_index, name='all_index'),
    path('manage_user/', views.manage_user, name='manage_user'),
    path('update_user/', views.update_user, name='update_user'),
    path('del_user/<int:id>', views.del_user, name='del_user')

]

