# -*- coding:utf-8 -*-
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, render_to_response
from django.views.generic.base import View

from article.models import Article, ChildTechnology


def index(request):
    if request.method == 'GET':
        articles = ChildTechnology.objects.all()
        articles1 = Article.objects.all()
        return render(request, 'web/index.html', {'articles': articles, 'articles1': articles1})

def about(request):
    if request.method == 'GET':
        articles = ChildTechnology.objects.all()
        return render(request, 'web/about.html', {'articles': articles})

def info(request, id):
    if request.method == 'GET':
        articles = ChildTechnology.objects.all()
        article = Article.objects.filter(pk=id).first()
        child = article.child_id
        cate = ChildTechnology.objects.filter(pk=child).first()
        return render(request, 'web/info.html', {'article': article, 'cate':cate, 'articles':articles})

def list(request):
    if request.method == 'GET':
        articles = ChildTechnology.objects.all()
        articles1 = Article.objects.all()
        return render(request, 'web/list.html', {'articles':articles,'articles1':articles1})

