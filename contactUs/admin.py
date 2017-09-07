#!/usr/bin/python
#-*- coding:utf-8 -*-
from django.contrib import admin

# Register your models here.
from contactUs.models import *

class EmailAdmin(admin.ModelAdmin):
    list_display = ('title', 'user_name','youremail','createtime')
    list_per_page = 10
    search_fields = ['title', 'content']
    list_filter = ['createtime']

# Register your models here.
admin.site.register(Email, EmailAdmin)