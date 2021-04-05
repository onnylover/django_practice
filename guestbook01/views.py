from django.http import HttpResponseRedirect
from django.shortcuts import render
from guestbook01 import models

# Create your views here.

def index(request):
    results = models.findall()
    data = {
        "results": results
    }
    return render(request, "guestbook01/index.html", data)

def add(request):
    name = request.POST["name"]
    password = request.POST["password"]
    message = request.POST["message"]
    models.insert(name,password,message)
    return HttpResponseRedirect("/guestbook01")

def deleteform(request):
    return render(request, "guestbook01/deleteform.html")

def delete(request):
    no = request.POST.get('no', None)
    password = request.POST["password"]
    models.deletebynoandpw(no, password)
    return HttpResponseRedirect("/guestbook01")

