from django.conf.urls import include, url
from django.contrib import admin
from booktest import views
urlpatterns = [
    url(r'^set_session$',views.set_session),
    url(r'^get_session$',views.get_session),
]
