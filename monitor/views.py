#!/usr/bin/python
# -*- coding: utf-8 -*-
from monitor.models import Disk
from django.http import JsonResponse
from django.core.mail import EmailMultiAlternatives
import time
from django.utils.timezone import now, timedelta
import psutil
import pytz
import datetime
from django.views.decorators.csrf import csrf_exempt
def save_disk_msg(request):
    try:
        result = psutil.disk_usage('/')
        disk_total = (result.total) / 1024 / 1024 / 1024
        disk_used = (result.used) / 1024 / 1024 / 1024
        diak_canuse = (result.free) / 1024 / 1024 / 1024
        percent = result.percent
        pro_name='cdsh_test'
        ip='192.168.1.2'
        now_time=time.strftime('%H:%M:%S', time.localtime(time.time()))
        print now_time
        # if now_time <='00:30:00':
        #     disk=Disk.objects.create(pro_name=str(pro_name),disk_total=str(disk_total),disk_used=str(disk_used),diak_canuse=str(diak_canuse),ip=str(ip),percent=str(percent))
        #     disk.save()
        now_time_return = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        data={'pro_name':'test','disk_total':disk_total,'disk_used':disk_used,'diak_canuse':diak_canuse,'percent':percent,'ip':ip,'time':now_time_return}
        return JsonResponse({'status': 200, 'message': 'success','data':data})
    except:
        return JsonResponse({'status': 200, 'message': 'failed', 'data': "接口数据异常"})


def sendSimpleEmail(request):
    try:
        # date = now().date() + timedelta(days=0)
        date=datetime.datetime.utcnow().replace(tzinfo=pytz.utc).astimezone(pytz.timezone('Asia/Shanghai'))

        # end = start + timedelta(days=1)
        disk_msgs=Disk.objects.filter(createtime__gt=date)
        print disk_msgs
        subject = u"磁盘剩余容量统计%s" % str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        from_email = "mzm5466@163.com"
        text_content = u"请即时使用本链接，重置您的密码"
        list_mail=[]
        for i, disk in enumerate(disk_msgs):
            # 需要修改链接地址，http://127.0.0.1:8888/部分 20171016
            html_content = u"<div><table border=‘1’><tr style=’color:#4169e1;font-size:20px‘><th>序号</th>\
            <th>项目名称</th><th>硬盘总容量</th><th>硬盘已使用容量</th><th>硬盘剩余容量</th><th>使用的百分比</th>\
            <th>ip地址</th></tr><tr><td>"+str(i+1)+"</td><td>"+disk.pro_name+"</td><td>"+disk.disk_total+"</td>\
            <td>"+disk.disk_used+"</td><td>"+disk.diak_canuse+"</td><td>"+disk.percent+"</td><td>"+disk.ip+"</td></tr></table></div>"
            list_mail.append(html_content)
        user_link = ''.join(list_mail)
        msg = EmailMultiAlternatives(subject, text_content, from_email, [from_email,'535135568@qq.com'])
        msg.attach_alternative(user_link, "text/html")
        msg.send()
        return JsonResponse({'status': 200, 'message': 'success'})
    except:
        return JsonResponse({'status': 200, 'message': 'failed', 'data': "接口数据异常"})

@csrf_exempt
def pro_name(request):
    list_name=[]
    proNames = Disk.objects.distinct().values("pro_name").order_by("pro_name")
    for pro_name in proNames:
        list_name.append(pro_name)
    return JsonResponse({'status': 200, 'message': 'failed', 'data': list_name})


@csrf_exempt
def pro_every(request):
    pro_name = request.GET['pro_name']
    data = Disk.objects.filter(pro_name=pro_name)[0]
    result = {'pro_name': pro_name, 'disk_total': data.disk_total, 'disk_used': data.disk_used, 'diak_canuse': data.diak_canuse,'percent': data.percent, 'ip': data.ip, 'time': data.createtime}
    return JsonResponse({'status': 200, 'message': 'failed', 'data': result})

@csrf_exempt
def math_percent(request):
    pro_name=request.GET['pro_name']
    list_percent=[]
    pro_percent=Disk.objects.filter(pro_name=pro_name)
    for percent in pro_percent:
        collection = {}
        collection['percent']=percent.percent
        collection['month'] = str(percent.createtime)[5:10]
        list_percent.append(collection)
    return JsonResponse({'status': 200, 'message': 'success', 'data': list_percent})
