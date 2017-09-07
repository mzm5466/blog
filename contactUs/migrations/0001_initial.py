# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default='\u8bf7\u5728\u6b64\u8f93\u5165\u6807\u9898', max_length=30, verbose_name='\u7559\u8a00\u6807\u9898')),
                ('content', models.TextField(default='\u8bf7\u5728\u6b64\u5904\u8f93\u5165', max_length=1000, verbose_name='\u7559\u8a00\u5185\u5bb9')),
                ('user_name', models.CharField(default='\u533f\u540d', max_length=20, verbose_name='\u4f60\u7684\u6635\u79f0')),
                ('youremail', models.CharField(default='\u4fdd\u5bc6', max_length=20, verbose_name='\u8054\u7cfb\u65b9\u5f0f')),
                ('createtime', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-createtime'],
                'verbose_name': '\u535a\u5ba2\u7559\u8a00',
                'verbose_name_plural': '\u535a\u5ba2\u7559\u8a00',
            },
        ),
    ]
