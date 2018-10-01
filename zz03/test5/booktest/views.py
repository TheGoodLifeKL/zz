from django.shortcuts import render,redirect
from django.conf import settings
from django.http import HttpResponse,JsonResponse
from booktest.models import AreaInfo
# Create your views here.

# EXCLUDE_IPS = ['192.168.21.71']
# def block_ips(view_func):
#     def wrapper(request,*args,**kwargs):
#         user_ip = request.META['REMOTE_ADDR']
#         print(user_ip)
#         if user_ip in EXCLUDE_IPS:
#             return HttpResponse('<h1>Forbidden</h1>')
#         else:
#             return view_func(request,*args,**kwargs)
#     return wrapper


# @block_ips
def static_test(request):
    print(settings.STATICFILES_FINDERS)
    return render(request,'booktest/static_test.html')

# @block_ips
def index(request):
    print('index')
    return render(request,'booktest/index.html')

def areas(request):
    area = AreaInfo.objects.get(atitle='合肥市')
    parent = area.aparent
    child = area.areainfo_set.all()
    return render(request,'booktest/areas.html',{'area':area,'parent':parent,'children':child})


def show_areas(request):
    return render(request,'booktest/show_areas.html')

def prov(request):
    areas = AreaInfo.objects.filter(aparent__isnull=True)
    areas_list = []
    for area in areas:
        areas_list.append((area.id,area.atitle))
    return JsonResponse({'data':areas_list})


def city(request,pid):
    areas = AreaInfo.objects.filter(aparent__id=pid)
    areas_list = []
    for area in areas:
        areas_list.append((area.id,area.atitle))
    return JsonResponse({'data':areas_list})

def dis(request,cid):
    areas = AreaInfo.objects.filter(aparent__id=cid)
    areas_list = []
    for area in areas:
        areas_list.append((area.id,area.atitle))
    return JsonResponse({'data':areas_list})

