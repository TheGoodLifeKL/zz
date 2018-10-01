from django.conf.urls import url
from booktest import views

urlpatterns = [
    url(r'^index$',views.index),
    # url(r'^showarg(\d+)$', views.show_arg),# 位置参数
    url(r'^showarg(?P<num>\d+)$', views.show_arg),# 捕获url参数:关键字参数
    url(r'^login$', views.login),
    url(r'^login_check$', views.login_check),
    url(r'^test_ajax$', views.ajax_test),
    url(r'^ajax_handle$', views.ajax_handle),
    url(r'^login_ajax$', views.login_ajax),
    url(r'^login_ajax_check$', views.login_ajax_check),
    url(r'^set_cookie$', views.set_cookie),
    url(r'^get_cookie$', views.get_cookie),
    url(r'^set_session$', views.set_session),
    url(r'^get_session$', views.get_session),
    url(r'^clear_session$', views.clear_session),
]
