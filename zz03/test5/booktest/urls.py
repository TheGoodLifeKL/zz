from django.conf.urls import url
from django.contrib import admin
from booktest import views
urlpatterns = [
    url(r'^static_test',views.static_test),
    url(r'^index$',views.index),
    url(r'^areas$',views.areas),
    url(r'^show_areas$',views.show_areas),
    url(r'^prov$',views.prov),
    url(r'^city(\d+)$',views.city),
    url(r'^dis(\d+)$',views.dis),
]

