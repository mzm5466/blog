#!/usr/bin/python
#-*- coding:utf-8 -*-
from django.conf.urls import url
from . import views
from blog import settings

urlpatterns = [
    url(r'^email/$',views.email,name="email"),
    url(r'^email_input/$', views.email_input,name="email_input"),

]
