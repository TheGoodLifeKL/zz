from django.conf.urls import include, url
from django.contrib import admin
from login import views
urlpatterns = [
    url(r'^login.html$',views.login)
]
