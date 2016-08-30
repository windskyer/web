#coding: utf-8
from django.conf.urls import url
from django.conf.urls import include

from . import views

urlpatterns = [
        # ex: /wvpn/
        url(r'^$', views.index, name='index'),
        url(r'^login/$', views.login, name='login'),
        url(r'^logout/$', views.logout, name='logout'),
]

app_name = 'wvpn'
