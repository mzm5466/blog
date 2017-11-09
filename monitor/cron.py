# !/usr/bin/env python3
# coding: utf-8
import urllib2,json,time
import pymysql
from monitor.m_settings import TASK_HOST
def url_visitor():
    url = "http://%s/monitor/email_disk/" % TASK_HOST
    req = urllib2.Request(url)
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    print res


def url_save_disk(url):
    connection = pymysql.connect(host='106.14.118.36',
                                 port=3306,
                                 user='root',
                                 password='mzm3433090123',
                                 db='blog',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    req = urllib2.Request(url)
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    result = json.loads(res)
    data= result["data"]
    disk_total = data['disk_total']
    disk_used = data['disk_used']
    diak_canuse = data['diak_canuse']
    percent = data['percent']
    pro_name = data['pro_name']
    ip = data['ip']
    createtime=data['time']
    print time
    if json.loads(res)['message']!="success":
        url_visitor()
    # 执行sql语句
    try:
        with connection.cursor() as cursor:
            # 执行sql语句，插入记录
            sql = 'INSERT INTO monitor_disk (pro_name, disk_total, disk_used, diak_canuse, percent,ip,createtime) VALUES (%s, %s, %s, %s, %s,%s,%s)'
            cursor.execute(sql, (pro_name, disk_total, disk_used, diak_canuse, percent,ip,createtime));
        # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
        connection.commit()

    finally:
        connection.close();




def url_visitor_collection():
    url_save_disk("http://%s/monitor/save_disk/" % TASK_HOST)  #测试服务器
