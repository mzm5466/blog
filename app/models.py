#!/usr/bin/python
#-*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from DjangoUeditor.models import UEditorField
from django.core.urlresolvers import reverse
KIND_CHOICES=(
    ('python','python'),
    ('c++','c++'),
    ('java','java'),
('javascript','javascript'),
('html','html'),
('css','css'),
('linux','linux'),
)

# Create your models here.
class Moment(models.Model):
    title=models.CharField(u'标题',max_length=30,default="请在此输入标题")
    shortcontent=models.TextField(u'短梗概',max_length=100,default="请在此输入梗概")
    content = UEditorField(u'内容', height=300, width=1000,
                           default=u'', blank=True, imagePath="",
                           toolbars='full', filePath='')#models.TextField(u'内容',max_length=3000,default="请在此处输入")
    user_name=models.CharField(u'作者',max_length=20,default='匿名')
    kind=models.CharField(u'文章类型',max_length=20,choices=KIND_CHOICES,default=KIND_CHOICES[0])
    createtime=models.DateTimeField(auto_now=True)
    def __unicode__(self):  # 在Python3中用 __str__ 代替 __unicode__
        return self.title

    class Meta:
        verbose_name = '博客文章'
        verbose_name_plural = '博客文章'
        ordering = ['-createtime']


