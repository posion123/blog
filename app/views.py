# -*- coding:utf-8 -*-
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, render_to_response
from django.urls import reverse
from django.views.generic.base import View
from django.http import HttpResponseRedirect

from app.models import Message
from article.models import Article, ChildTechnology


# 首页
from photo.models import Photoes


def index(request):
    if request.method == 'GET':
        articles = ChildTechnology.objects.all()
        articles1 = Article.objects.all()[:6]
        photoes = []
        photoes1 = Photoes.objects.filter(title='一个人的旅行').first()
        photoes2 = str(photoes1.content)
        photoes3 = photoes2.split('>')[:6]
        for p in photoes3:
            photoes.append(p + '>')
        return render(request, 'web/index.html', {'articles': articles, 'articles1': articles1, 'photoes':photoes})

#关于我的信息
def about(request):
    if request.method == 'GET':
        articles = ChildTechnology.objects.all()
        articles1 = Article.objects.all()[:6]
        photoes = []
        photoes1 = Photoes.objects.filter(title='一个人的旅行').first()
        photoes2 = str(photoes1.content)
        photoes3 = photoes2.split('>')[:6]
        for p in photoes3:
            photoes.append(p + '>')
        return render(request, 'web/about.html', {'articles': articles, 'articles1':articles1, 'photoes': photoes})

#显示对应文章的内容
def info(request, id):
    if request.method == 'GET':
        articles = ChildTechnology.objects.all()
        article = Article.objects.filter(pk=id).first()
        child = article.child_id
        cate = ChildTechnology.objects.filter(pk=child).first()
        articles1 = Article.objects.all()[:6]
        return render(request, 'web/info.html', {'article': article, 'cate':cate, 'articles':articles,'articles1':articles1})

#显示所有文章
def list(request):
    if request.method == 'GET':

        articles = ChildTechnology.objects.all()
        articles1 = Article.objects.all()[:6]
        articles2 = Article.objects.all()
        page = request.GET.get('page', 1)
        pg = Paginator(articles2, 4)
        articles2 = pg.page(page)
        return render(request, 'web/list.html', {'articles':articles,'articles1':articles1, 'articles2':articles2})

#点击对应的文章分类,显示对应文章的列表
def my_list(request, id):
    if request.method == 'GET':
        c_article = ChildTechnology.objects.filter(pk=id).first()
        all_article = c_article.article_set.all()
        articles1 = Article.objects.all()[:6]
        articles = ChildTechnology.objects.all()
        return render(request, 'web/list.html', {'all_article':all_article,'articles1':all_article, 'articles':articles})


# 显示所有相册信息
def all_photoes(request):
    if request.method == 'GET':
        photoes1 = Photoes.objects.all()
        photoes = []
        for photo in photoes1:
            photoes.append([str(photo.content).split('>')[0] + '>', photo.title, photo.desc, photo.id])
        return render(request, 'web/share.html', {'photoes': photoes})

# 个人相册
def person_photoes(request, id):
    if request.method == 'GET':
        photoes=[]
        photoes1 = Photoes.objects.filter(pk=id).first()
        photoes2 = str(photoes1.content)
        photoes3 = photoes2.split('>')
        for p in photoes3:
            photoes.append(p + '>')
        photoes = photoes[:len(photoes)-1]
        return render(request, 'web/all_photoes.html', {'photoes': photoes})

# 留言
def message(request):
    if request.method == 'GET':
        articles = ChildTechnology.objects.all()
        articles1 = Article.objects.all()[:6]
        messages = Message.objects.all()
        photoes = []
        photoes1 = Photoes.objects.filter(title='一个人的旅行').first()
        photoes2 = str(photoes1.content)
        photoes3 = photoes2.split('>')[:6]
        for p in photoes3:
            photoes.append(p + '>')
        return render(request, 'web/gbook.html', {'articles': articles, 'articles1': articles1, 'photoes': photoes, 'messages': messages})

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        content = request.POST.get('lytext')
        Message.objects.create(name=name,
                               email=email,
                               content=content)
        return HttpResponseRedirect(reverse('app:message'))