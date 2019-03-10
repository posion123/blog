from django.shortcuts import render

from django.http import HttpResponseRedirect
# Create your views here.
from django.urls import reverse

from app.models import Message


# 收到的信息
def message(request):
    if request.method == 'GET':
        # 查询数据库answer字段是否为空
        mess = Message.objects.filter(answer__isnull=True)
        mess1 = len(mess)
        # 返回数据
        message = Message.objects.all()
        return render(request, 'message.html', {'message': message, 'mess1': mess1})


# 回复
def answer(request, id):
    if request.method == 'GET':
        message = Message.objects.filter(id=id).first()
        mess = Message.objects.filter(answer__isnull=True)
        mess1 = len(mess)
        return render(request, 'answer.html', {'message': message, 'mess1': mess1})
    if request.method == 'POST':
        answer = request.POST.get('answer')
        message = Message.objects.filter(id=id).first()
        message.answer = answer
        message.save()
        return HttpResponseRedirect(reverse('message:message'))


# 删除回复
def del_message(request, id):
    Message.objects.filter(id=id).delete()
    return HttpResponseRedirect(reverse('message:message'))



