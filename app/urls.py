#!/usr/bin/python
#-*- coding:utf-8 -*-
from django.conf.urls import url
from . import views
from blog import settings

urlpatterns = [
    url(r'moments_input', views.moments_input),
    # url(r'', views.welcome),
    url(r'^blog/$',views.blog,name='blog'),
    url(r'^index/$',views.index2,name='index2'),
    url(r'^gallery/$',views.gallery,name='gallery'),
    url(r'^single/(\d+)$', views.single,name='single'),
    url(r'^about/$', views.about, name='about'),
    url(r'^header/$',views.header,name="header"),
    url(r'^message/$',views.message,name="message"),
    url(r'^sloiderbar/$',views.sloiderbar,name='sloiderbar'),
    url(r'^search_article/$', views.search_article, name='search_article'),
    url( r'^static/(?P<path>.*)$', 'django.views.static.serve',{ 'document_root': settings.STATIC_URL }),
]
