#!/usr/bin/python
#coding:utf-8
from django.contrib import admin
from app.models import *

class MomentAdmin(admin.ModelAdmin):
    list_display = ('title', 'user_name','kind','createtime')
    list_per_page = 10
    search_fields = ['title', 'content']
    list_filter = ['createtime', 'kind']

# Register your models here.
admin.site.register(Moment, MomentAdmin)