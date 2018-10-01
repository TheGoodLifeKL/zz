from django.conf.urls import url
from django.contrib import admin
from stu_manageapp import views
urlpatterns = [
    url(r'^class$',views.show_clsinfo),
    url(r'^classdetail/(\d+)$',views.classdetail),
    url(r'^delete/(\d+)/(\d+)$',views.delete_stu),
]
