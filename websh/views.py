#-*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from .forms import AddForm
import time
import os
import psutil
# Create your views here.
def index(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        #获取服务器信息信息
        #cpu信息
        cpu = psutil.cpu_times(percpu=True)
        #获取单项数据信息，如用户user的cpu时间比
        cpu
        mem = psutil.virtual_memory()
        mem.total
        mem.used
        mem.percent
        return HttpResponse([cpu,",mem: " ,mem])
    else:
        form = AddForm()
    return render(request,'hello.html',{'form':form})


    return render(request,'hello.html')

'''
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a) + int(b)))'''



