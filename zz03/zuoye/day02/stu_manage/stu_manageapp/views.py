from django.shortcuts import render,redirect
from django.http import HttpResponse
from stu_manageapp.models import ClassInfo,StudentInfo
# Create your views here.
def show_clsinfo(request):
    all_cls = ClassInfo.objects.all()
    cls_count = all_cls.count()
    return render(request,'show_cls.html',{'all_cls':all_cls,'cls_count':cls_count})


def classdetail(request,cid):
    cls = ClassInfo.objects.get(id=cid)
    all_stu = StudentInfo.objects.filter(stu_class=cls)
    cls.stu_num = all_stu.count()
    cls.save()
    return render(request,'cls_detail.html',{'cls':cls,'all_stu':all_stu})


def delete_stu(request,cid,sid):
    st = StudentInfo.objects.get(id=sid)
    st.delete()
    return redirect('/stu/classdetail/'+cid)
    # return HttpResponse('ok')