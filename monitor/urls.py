#!/usr/bin/python
#-*- coding:utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^save_disk/$', views.save_disk_msg,name="save_disk_msg"),
    url(r'^email_disk/$', views.sendSimpleEmail, name="snedemail"),
    url(r'^proname_disk/$', views.pro_name, name="pro_name"),
    url(r'^percent_disk/$', views.math_percent, name="math_percent"),
    url(r'^proevery_disk/$', views.pro_every, name="pro_every"),
]
