#!/usr/bin/python
#-*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Email(models.Model):
    title = models.CharField(u'留言标题', max_length=30, default="请在此输入标题")
    content =  models.TextField(u'留言内容',max_length=1000,default="请在此处输入")
    user_name = models.CharField(u'你的昵称', max_length=20, default='匿名')
    youremail = models.CharField(u'联系方式', max_length=20,default="保密")
    createtime = models.DateTimeField(auto_now=True)

    def __unicode__(self):  # 在Python3中用 __str__ 代替 __unicode__
        return self.title

    class Meta:
        verbose_name = '博客留言'
        verbose_name_plural = '博客留言'
        ordering = ['-createtime']
