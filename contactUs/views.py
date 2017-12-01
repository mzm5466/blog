#!/usr/bin/python
#-*- coding:utf-8 -*-
from django.shortcuts import render
from contactUs.forms import EmailForm
from django.http import HttpResponseRedirect,JsonResponse
from django.core.urlresolvers import reverse
# Create your views here.
from django.core.mail import send_mail
import os
from models import *
from django.views.decorators.csrf import csrf_exempt
def email(request):
    send_mail(u'[留言]', u'我的测试.', 'mzm5466@163.com',
              ['535135568@qq.com'], fail_silently=False)
    return render(request,"about.html")
def email_input(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            # title = request.POST['title']
            # content = request.POST['content']
            # user_name = request.POST['user_name']
            # youremail = request.POST['youremail']
            # send_mail('['+user_name.encode('utf-8')+'的留言]', 'from:'+youremail.encode('utf-8')+'\n'+title.encode('utf-8')+'\n内容：'+content.encode('utf-8')+'.', '1107771338@qq.com',
            #           ['1107771338@qq.com'], fail_silently=False)
            moment = form.save()
            moment.save()
            return HttpResponseRedirect(reverse('email_input'))
    else:
        form = EmailForm()
    return render(request,'chatme.html', {'form': form})
@csrf_exempt
def errorLog(request):
    errorMessage=request.GET.get('errorMessage','')
    scriptURI = request.GET.get('scriptURI',''),
    lineNumber = request.GET.get('lineNumber','')
    columnNumber = request.GET.get('columnNumber','')
    errorObj =request.GET.get('errorObj','')
    try:
        result=ErrorLog.objects.create(errorMessage=errorMessage,scriptURI=scriptURI,lineNumber=lineNumber,columnNumber=columnNumber,errorObj=errorObj)
        result.save()
    except:
        print "error!"

    return JsonResponse({'status':200,'message':'success'})