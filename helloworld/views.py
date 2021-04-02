from django.shortcuts import render
from django.http import  HttpResponse

# Create your views here.

def hello1(request):
    return HttpResponse("<h1>hello world</h1><h2>哈嘍</h2><h3>欢迎</h3>", content_type="text/html;charset=utf-8")

def hello2(request):
    #results = model.findall()
    return render(request, 'helloworld/hello2.html',{})

def tags(request):
    #results = model.findall()
    return render(request, 'helloworld/tags.html',{})