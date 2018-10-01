from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def set_session(request):
    request.session['username'] = 'smart'
    request.session['age'] = 18

    return HttpResponse('设置session')


def get_session(request):
     username = request.session['username']
     age = request.session['age']

     return HttpResponse(username+':'+str(age))
