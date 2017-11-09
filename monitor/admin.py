#!/usr/bin/python
#-*- coding:utf-8 -*-
from django.contrib import admin

# Register your models here.
from monitor.models import *

class DiskAdmin(admin.ModelAdmin):
    list_display = ('pro_name', 'disk_total','disk_used','diak_canuse','createtime','ip','percent')
    list_per_page = 10
    search_fields = ['pro_name']
    list_filter = ['createtime','percent']

# Register your models here.
admin.site.register(Disk, DiskAdmin)