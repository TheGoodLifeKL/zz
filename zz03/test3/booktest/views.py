from django.shortcuts import render,redirect
from booktest.models import BookInfo
from django.http import HttpResponse
# Create your views here.

def login_required(view_func):
    def wrapper(request,*args,**kwargs):
        if request.session.has_key('islogin'):
            return view_func(request,*args,**kwargs)
        else:
            return redirect('/login')
    return wrapper

def index(request):
    return render(request,'booktest/index.html')


def temp_var(request):
    my_dict = {'title':'字典键值'}
    my_list = [1,2,3]
    book = BookInfo.objects.get(id=1)
    return render(request,'booktest/temp_var.html',{'my_dict':my_dict,'my_list':my_list,'book':book})


def temp_tags(request):
    '''模板标签'''
    books = BookInfo.objects.all()
    return render(request,'booktest/temp_tags.html',{'books':books})


def temp_filter(request):
    '''模板过滤器'''
    books = BookInfo.objects.all()
    return render(request,'booktest/temp_filter.html',{'books':books})


def temp_child(request):
    return render(request,'booktest/child.html')


def html_escape(request):
    return render(request,'booktest/html_escape.html',{'content':'<h1>hello</h1>'})

def login(request):
    '''显示登录页面'''
    if request.session.has_key('islogin'):
        return redirect('/change_pwd')
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
        response = redirect('/change_pwd')
        if remember == 'on':
            response.set_cookie('username',username,max_age=7*24*3600)
            response.set_cookie('password',password,max_age=7*24*3600)
        request.session['islogin'] = True
        request.session['username'] = username
        return response
    else:
        return redirect('/login')
    # 返回应答



@login_required
def change_pwd(request):
    # # 进行用户是否登录的判断
    # if not request.session.has_key('islogin')
    #     return redirect('/login')
    return render(request,'booktest/change_pwd.html')

@login_required
def change_pwd_action(request):
    pwd = request.POST.get('pwd')
    username = request.session.get('username')
    return HttpResponse('%s修改密码为:%s'%(username,pwd))





