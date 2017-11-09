#!/usr/bin/python
#-*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Disk(models.Model):
    pro_name=models.CharField(max_length=30,blank=True, null=True,verbose_name=u"项目名称")
    disk_total = models.CharField(max_length=80, blank=True, null=True, verbose_name=u'磁盘总空间')
    disk_used = models.CharField(max_length=80, blank=True, null=True, verbose_name=u'磁盘已用空间')
    diak_canuse= models.CharField(max_length=80, blank=True, null=True, verbose_name=u'磁盘剩余空间')
    createtime = models.DateTimeField(auto_now=True,verbose_name=u'记录生成时间')
    ip=models.CharField(max_length=80, blank=True, null=True, verbose_name=u'服务器ip')
    percent = models.CharField(max_length=80, blank=True, null=True, verbose_name=u'使用率')
    def __unicode__(self):  # 在Python3中用 __str__ 代替 __unicode__
        return self.pro_name

    class Meta:
        verbose_name = '岸登运维磁盘容量监控'
        verbose_name_plural = '磁盘容量监控'
        ordering = ['-createtime']
