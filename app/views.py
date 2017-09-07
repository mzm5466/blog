#!/usr/bin/python
#-*- coding:utf-8 -*-
import os
from app.forms import MomentForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from app.models import *
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render,render_to_response
from django.utils.safestring import mark_safe

from django.template import RequestContext
from django.views.generic import *

from django .db.models.aggregates import Count

from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import json
import os
import datetime
#分页
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def welcome(request):
    return HttpResponse("<h1>我的测试</h1>")


def moments_input(request):
    if request.method == 'POST':
        form = MomentForm(request.POST)
        if form.is_valid():
            moment = form.save()
            moment.save()
            return HttpResponseRedirect(reverse("app.views.welcome"))
    else:
        form = MomentForm()
    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return render(request, os.path.join(PROJECT_ROOT, 'app/templates', 'moments_input.html'), {'form': form})


def blog(request):
    lists_all = Moment.objects.order_by("-createtime")  # 将User表中的所有对象赋值给users这个变量，它是一个列表

    paginator = Paginator(lists_all, 5) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    return render(request, 'blog.html', {'lists': contacts})  # 生成一个user变量，这个变量可以给templates中的html文件使用

def index2(request):
    top3=Moment.objects.all().order_by('-createtime')[:3]
    return render(request, "index2.html",{"top3":top3})


def gallery(request):
    return render(request, "gallery.html")


def single(request,id):
    list_detail = Moment.objects.get(id=id)
    pageHtml = mark_safe(list_detail.content)
    ret = {"pageHtml":pageHtml,"list_detail": list_detail}
    return render(request, "single.html", ret)
    # return render_to_response("single.html",context={"list_detail":list_detail})

def about(request):
    return render(request,"about.html")

def header(request):
    return render(request,"header.html")

def message(request):
    return render(request,"chatme.html")

@csrf_exempt
def search_article(request):
    if request.method == "GET":
            search = request.POST.get('name')
            print search
            lists = Moment.objects.filter(title=search,content=search,kind=search)
            return render(request, "search.html",{'lists': lists})

def sloiderbar(request):
    top3 = Moment.objects.all().order_by('-createtime')[:3]
    return render_to_response(request, "sloiderbar.html", {"top3": top3})
