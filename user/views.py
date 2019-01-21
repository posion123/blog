from django.core.paginator import Paginator
from django.shortcuts import render

from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.
from django.urls import reverse

from article.models import Article
from user.models import User


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        userpwd = request.POST.get('userpwd')
        user = User.objects.filter(s_name=username).first()
        if user:
            if user.password == userpwd:
                print(user.id)
                request.session['user_id'] = user.id
                return HttpResponseRedirect(reverse('user:index'))
            else:
                message1 = '密码不对'
                return render(request, 'login.html', {'message1':message1})
        else:
            message = '没有该用户请先注册'
            return render(request, 'login.html', {'message': message})

def index(request):
    if request.method == 'GET':
        return all_index(request)

def logout(request):
    if request.method =='GET':
        request.session.flush()
    return HttpResponseRedirect(reverse('user:login'))

def all_index(request):
    if request.method == 'GET':
        all_data2 = Article.objects.all()
        page = request.GET.get('page', 1)
        pg = Paginator(all_data2, 5)
        all_data2 = pg.page(page)
        return render(request, 'index.html', {'all_data2':all_data2})

def add_article(request):
    if request.method == 'GET':
        return render(request, 'add-article.html')