from django.core.paginator import Paginator
from django.shortcuts import render

from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.
from django.urls import reverse

from app.models import Message
from article.models import Article
from user.models import User


# 登录
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

# 首页
def index(request):
    if request.method == 'GET':
        return all_index(request)

# 退出
def logout(request):
    if request.method =='GET':
        request.session.flush()
    return HttpResponseRedirect(reverse('user:login'))

# 首页文章进行分页操作
def all_index(request):
    if request.method == 'GET':
        mess = Message.objects.filter(answer__isnull=True)
        mess1 = len(mess)
        all_data2 = Article.objects.all()
        page = request.GET.get('page', 1)
        pg = Paginator(all_data2, 5)
        all_data2 = pg.page(page)
        return render(request, 'index.html', {'all_data2':all_data2, 'mess1': mess1})

# 添加文章
def add_article(request):
    if request.method == 'GET':
        return render(request, 'add-article.html')

def manage_user(request):
    if request.method == 'GET':
        user = User.objects.all()
        arts = Article.objects.all()
        art = len(arts)
        mess = Message.objects.filter(answer__isnull=True)
        mess1 = len(mess)

        return render(request, 'manage-user.html', {'users': user, 'art': art, 'mess1': mess1})


def update_user(request):
    if request.method == 'GET':
        user = User.objects.filter(id=1).first()
        return render(request, 'update_user.html', {'user': user})

    if request.method == 'POST':
        name = request.POST.get('username')
        tel = request.POST.get('usertel')
        old_password = request.POST.get('old_password')
        newpassword = request.POST.get('password')
        newpassword1 = request.POST.get('new_password')
        user = User.objects.filter(id=1).first()
        if user.password == old_password:
            if newpassword == newpassword1:
                user.s_name = name
                user.tel = tel
                user.password = newpassword
                user.save()
                return HttpResponseRedirect(reverse('user:manage_user'))
            else:
                message = '输入的两次密码不相同'
                return  render(request, 'update_user.html', {'message1': message})
        else:
            message = '你输入的密码不对'
            return render(request, 'update_user.html', {'message': message})

def del_user(request, id):
    User.objects.filter(id=id).first().delete()

    return HttpResponseRedirect(reverse('user:manage_user'))
