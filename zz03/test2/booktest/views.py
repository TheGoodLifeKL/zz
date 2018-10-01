from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
# Create your views here.

def index(request):
    return render(request,'booktest/index.html')

def show_arg(request,num):
    return HttpResponse(num)

def login(request):
    '''显示登录页面'''
    if request.session.has_key('islogin'):
        return redirect('/index')
    else:
        if 'username' in request.COOKIES:
            username = request.COOKIES['username']
        else:
            username = ''
        if 'password' in request.COOKIES:
            password = request.COOKIES['password']
        else:
            password = ''
        return render(request,'booktest/login.html',{'username':username,'password':password})

def login_check(request):
    # 获取提交的用户和密码
    # print(type(request.POST))
    username = request.POST.get('username')
    password = request.POST.get('password')
    remember = request.POST.get('remember')
    # 进行登录验证
    if username == 'smart' and password == '123':
        response = redirect('/index')
        if remember == 'on':
            response.set_cookie('username',username,max_age=7*24*3600)
            response.set_cookie('password',password,max_age=7*24*3600)
        request.session['islogin'] = True
        return response
    else:
        return redirect('/login')
    # 返回应答


def ajax_test(request):
    '''显示ajax页面'''
    return render(request,'booktest/test_ajax.html')

def ajax_handle(request):
    return JsonResponse({'res':1})

def login_ajax(request):
    return render(request,'booktest/login_ajax.html')

def login_ajax_check(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if username == 'smart' and password == '123':
        return JsonResponse({'res':1})
    else:
        return JsonResponse({'res':0})

def set_cookie(request):
    response = HttpResponse('设置cookie')
    # response.set_cookie('num',1,max_age=14*24*3600)
    response.set_cookie('num',1)
    return response


def get_cookie(request):
    num = request.COOKIES['num']
    return HttpResponse(num)

def set_session(request):
    request.session['username'] = 'smart'
    request.session['age'] = 18
    return HttpResponse('设置session')


def get_session(request):
    username = request.session['username']
    age = request.session['age']
    return HttpResponse(username+':'+str(age))


def clear_session(request):
    request.session.clear()
    return HttpResponse('清除成功')



