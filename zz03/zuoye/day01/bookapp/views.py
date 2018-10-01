from django.shortcuts import render
from bookapp.models import BookInfo
# Create your views here.
def book(request):
    books = BookInfo.objects.all()
    return render(request,'bookapp/book.html',{'books':books})