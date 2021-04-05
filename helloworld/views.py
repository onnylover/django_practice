from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello1(request):
    name = request.GET["name"]
    return HttpResponse(f"""<h1>hello world {name}</h1><h2>哈嘍</h2><h3>欢迎</h3><a href="/">Back to Main</a>""", content_type="text/html;charset=utf-8")

def main(request):
    #results = model.findall()
    return render(request, 'helloworld/main.html',{})

def tags(request):
    #results = model.findall()
    return render(request, 'helloworld/tags.html',{})

def form(request):
    return render(request, 'helloworld/form.html', {})

def join(request):
    #GET해서 딕셔너리를 만들어서 자료를 받음
    email = request.POST["email"]
    password = request.POST["password"]
    gender = request.POST["gender"]
    #hobbies = request.POST["hobbies"]
    hobbies = request.POST.getlist("hobbies")
    description = request.POST["desc"]
    print(email, password, gender, hobbies, description)
    return HttpResponse("<h1>This is join page</h1><h2>Join OK</h2>", content_type="text/html;charset=utf-8")