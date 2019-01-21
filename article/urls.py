from django.urls import path

from article import views

urlpatterns = [
    #编辑文章
    path(r'edit_article/', views.edit_article, name='edit_article'),
    #获取文章
    path(r'article/', views.article, name='article'),
    #添加栏目
    path('category/', views.category, name='category'),
    #显示栏目
    path('all_category/', views.all_category, name='all_category'),
    #添加文章
    path('all_edit/', views.all_edit, name='all_edit'),
    #删除文章
    path('del_article/<int:id>', views.del_article, name='del_article'),
    path('up_article/<int:id>', views.up_article, name='up_article'),
    #删除栏目
    path('del_category/<int:id>', views.del_category, name='del_category'),
    #测试
    path('look/', views.look, name='look'),
]