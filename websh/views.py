from django.shortcuts import render
from django.http import HttpResponse
from .forms import AddForm
import time
import os
# Create your views here.
def index(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        stime = time.time()
        os.open()
        return HttpResponse(stime)
    else:
        form = AddForm()
    return render(request,'hello.html',{'form':form})


    return render(request,'hello.html')

'''
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a) + int(b)))'''



