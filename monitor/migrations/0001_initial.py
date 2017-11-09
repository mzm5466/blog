# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disk',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pro_name', models.CharField(max_length=30, null=True, verbose_name='\u9879\u76ee\u540d\u79f0', blank=True)),
                ('disk_total', models.CharField(max_length=80, null=True, verbose_name='\u78c1\u76d8\u603b\u7a7a\u95f4', blank=True)),
                ('disk_used', models.CharField(max_length=80, null=True, verbose_name='\u78c1\u76d8\u5df2\u7528\u7a7a\u95f4', blank=True)),
                ('diak_canuse', models.CharField(max_length=80, null=True, verbose_name='\u78c1\u76d8\u5269\u4f59\u7a7a\u95f4', blank=True)),
                ('createtime', models.DateTimeField(auto_now=True, verbose_name='\u8bb0\u5f55\u751f\u6210\u65f6\u95f4')),
                ('ip', models.CharField(max_length=80, null=True, verbose_name='\u670d\u52a1\u5668ip', blank=True)),
                ('percent', models.CharField(max_length=80, null=True, verbose_name='\u4f7f\u7528\u7387', blank=True)),
            ],
            options={
                'ordering': ['-createtime'],
                'verbose_name': '\u5cb8\u767b\u8fd0\u7ef4\u78c1\u76d8\u5bb9\u91cf\u76d1\u63a7',
                'verbose_name_plural': '\u78c1\u76d8\u5bb9\u91cf\u76d1\u63a7',
            },
        ),
    ]
