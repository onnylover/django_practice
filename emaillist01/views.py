from django.shortcuts import render
from emaillist01 import models
from django.http import HttpResponseRedirect
#안쓰는거는 없애주는게 좋
#from django.http import HttpResponse

#from emaillist01.models import findall() 로도 가능함

# Create your views here.

def index(request):
    results = models.findall()
    data = {
        "results": results
    }
    return render(request, "emaillist01/index.html", data)

def form(request):
    return render(request, "emaillist01/form.html")

def add(request):
    firstname = request.POST["fn"]
    lastname = request.POST["ln"]
    email = request.POST["email"]

    models.insert(firstname,lastname,email)
    return HttpResponseRedirect("/emaillist01")

    #테스트 목적
    #print(firstname,lastname,email)
    #HTML 리턴
    #return HttpResponse("Append Sucsess", content_type="text/html;charset=utf-8")



