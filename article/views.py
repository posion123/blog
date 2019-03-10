from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from app.models import Message
from article.models import Article, FatherTechnology, ChildTechnology


# def test(request):
#     if request.method == 'GET':
#         return render(request, 'test.html')
#     if request.method == 'POST':
#         return HttpResponseRedirect(reverse('edit.html'))


# 编辑文章
def edit_article(request):
    """
    文章编辑方法
    """
    if request.method == 'GET':
        return all_edit(request)
    if request.method == 'POST':
        # 获取文章的标题和内容
        title = request.POST.get('title')
        content = request.POST.get('content')
        desc = request.POST.get('describe')
        category = request.POST.get('category')
        icon = request.FILES.get('titlepic')
        # 使用all()方法进行判断，如果文章标题和内容任何一个参数没有填写，则返回错误信息
        child = ChildTechnology.objects.filter(id=category).first()

        Article.objects.create(title=title,
                               content=content,
                               desc=desc,
                               child_id=child.id,
                               father_id=child.f_id,
                               icon=icon)
        # 创建文章成功后，跳转到文章列表页面
        return HttpResponseRedirect(reverse('user:index'))


# 显示所有文章
def article(request):
    if request.method == 'GET':
        # 获取所有的文章
        articles = Article.objects.all()
        return render(request, 'article.html', {'articles': articles})


# 获取栏目
def category(request):
    if request.method == 'GET':
        return all_category(request)
    if request.method == 'POST':
        name = request.POST.get('name')
        alias = request.POST.get('alias')
        fid = request.POST.get('sel')
        describe = request.POST.get('describe')
        if fid == '0':
            FatherTechnology.objects.create(f_name=name,
                                            f_alias=alias,
                                            f_desc=describe)
            return HttpResponseRedirect(reverse('article:category'))
        elif fid == '1':
            f_id = FatherTechnology.objects.filter(id=fid).first()
            ChildTechnology.objects.create(c_name=name,
                                           c_alias=alias,
                                           c_desc=describe,
                                           f_id=f_id.id)
            return HttpResponseRedirect(reverse('article:category'))
        elif fid == '2':
            f_id = FatherTechnology.objects.filter(id=fid).first()
            ChildTechnology.objects.create(c_name=name,
                                           c_alias=alias,
                                           c_desc=describe,
                                           f_id=f_id.id)
            return HttpResponseRedirect(reverse('article:category'))
        elif fid == '3':
            f_id = FatherTechnology.objects.filter(id=fid).first()
            ChildTechnology.objects.create(c_name=name,
                                           c_alias=alias,
                                           c_desc=describe,
                                           f_id=f_id.id)

            return HttpResponseRedirect(reverse('article:category'))

        elif fid == '4':
            f_id = FatherTechnology.objects.filter(id=fid).first()
            ChildTechnology.objects.create(c_name=name,
                                           c_alias=alias,
                                           c_desc=describe,
                                           f_id=f_id.id)

            return HttpResponseRedirect(reverse('article:category'))

# 显示所有栏目
def all_category(request):
    all_data = FatherTechnology.objects.all()
    mess = Message.objects.filter(answer__isnull=True)
    mess1 = len(mess)
    return render(request, 'category.html', {'all_data': all_data, 'mess1': mess1})


# 显示所有子栏目
def all_edit(request):
    all_data = ChildTechnology.objects.all()
    mess = Message.objects.filter(answer__isnull=True)
    mess1 = len(mess)
    return render(request, 'add-article.html', {'all_data': all_data, 'mess1': mess1})

# 删除文章
def del_article(request, id):
        Article.objects.filter(pk=id).delete()
        return HttpResponseRedirect(reverse('user:index'))


# 修改文章
def up_article(request, id):
    if request.method == 'GET':
        user = Article.objects.filter(pk=id).first()
        return render(request, 'update-article.html', {'user': user})
    if request.method == 'POST':
        user = Article.objects.filter(pk=id).first()
        title = request.POST.get('title')
        content = request.POST.get('content')
        describe = request.POST.get('describe')
        user.title = title
        user.content = content
        user.desc = describe
        user.save()
        return HttpResponseRedirect(reverse('user:index'))


# def up_article(request, id):
#     if request.method == 'GET':
#         return render(request, 'update.html')
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         Article.objects.filter(id=id).update(title=title)
#         return HttpResponseRedirect(reverse('user:index'))


# 删除栏目
def del_category(request, id):
    FatherTechnology.objects.filter(pk=id).delete()
    return HttpResponseRedirect(reverse('article:category'))


#修改栏目
def up_category(request, id):
    if request.method == 'GET':
        categorys = FatherTechnology.objects.filter(pk=id).first()
        all_data = FatherTechnology.objects.all()
        mess = Message.objects.filter(answer__isnull=True)
        mess1 = len(mess)
        return render(request, 'update-category.html', {'categorys': categorys, 'all_data': all_data, 'mess1': mess1})

    if request.method == 'POST':
        name = request.POST.get('name')
        alias = request.POST.get('alias')
        fid = request.POST.get('sel')
        describe = request.POST.get('describe')
        category = FatherTechnology.objects.filter(pk=id).first()
        category.f_name = name
        category.f_alias = alias
        category.f_desc = describe
        category.save()
        return HttpResponseRedirect(reverse('article:category'))

# 测试
def look(request):
    all_data2 = Article.objects.all()
    return render(request, 'test.html', {'all_data2':all_data2})

