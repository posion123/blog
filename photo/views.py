import base64
from pickle import dumps,loads

from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

#显示图片信息
from django.urls import reverse

from app.models import Message
from photo.models import Photoes, Mfile


# 相册列表
def photoes(request):
    if request.method == 'GET':
        page = request.GET.get('page', 1)
        photoes = Photoes.objects.all()
        pg = Paginator(photoes, 3)
        photoes = pg.page(page)
        mess = Message.objects.filter(answer__isnull=True)
        mess1 = len(mess)
        return render(request, 'notice.html', {'photoes': photoes, 'mess1': mess1})


# 添加相册
def add_photoes(request):
    if request.method == 'GET':
        mess = Message.objects.filter(answer__isnull=True)
        mess1 = len(mess)
        return render(request, 'add_photoes.html', {'mess1': mess1})
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        desc = request.POST.get('describe')
        Photoes.objects.create(title=title,
                               content=content,
                               desc=desc)
        return HttpResponseRedirect(reverse('photo:photoes'))

# 删除相册
def del_photoes(request, id):
    Photoes.objects.filter(pk=id).delete()
    return HttpResponseRedirect(reverse('photo:photoes'))

# 修改相册

def up_photoes(request, id):
    if request.method == 'GET':
        photoes = Photoes.objects.filter(pk=id).first()
        mess = Message.objects.filter(answer__isnull=True)
        mess1 = len(mess)
        return render(request, 'update-photoes.html', {'photoes': photoes, 'mess1': mess1})
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        desc = request.POST.get('describe')
        photo = Photoes.objects.filter(pk=id).first()
        photo.title = title
        photo.content = content
        photo.desc = desc
        photo.save()
        return HttpResponseRedirect(reverse('photo:photoes'))

# 文件操作
def my_file(request):
    if request.method == 'GET':
        mess = Message.objects.filter(answer__isnull=True)
        mess1 = len(mess)
        files = Mfile.objects.all()
        return render(request, 'my_file.html', {'files':files, 'mess1':mess1})
    if request.method == 'POST':

        name = request.FILES.get('pic')
        title = str(name)
        Mfile.objects.create(name=name, title=title)
        return HttpResponseRedirect(reverse('photo:my_file'))

# 文件删除
def del_my_file(request, id):
    if request.method == 'GET':
        Mfile.objects.filter(pk=id).delete()
        return HttpResponseRedirect(reverse('photo:my_file'))


# 测试
def test(request):
    if request.method == 'GET':
        photos = Photoes.objects.all()
        return render(request, 'test2.html')
