from django.conf.urls import url
from django.contrib import admin
from bookapp import views
urlpatterns = [
    url(r'^book$',views.book)
]
