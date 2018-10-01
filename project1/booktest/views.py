from django.shortcuts import render,redirect
from booktest.models import BookInfo
from datetime import date
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
def index(request):
    books = BookInfo.objects.all()
    return render(request,'booktest/index.html',{'books':books})

def create(request):
    b = BookInfo()
    b.btitle = '流星蝴蝶剑'
    b.bpub_date = date(1990,1,1)
    b.save()
    # return HttpResponse('OK')
    # return HttpResponseRedirect('/index')
    return redirect('/index')
def delete(request,bid):
    # 1.通过bid获取图书对象
    b = BookInfo.objects.get(id=bid)
    # 2.删除
    b.delete()
    # 3.重定向,让浏览器返回/index
    # return HttpResponseRedirect('/index')
    return redirect('/index')