from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from emaillist02.models import Emaillist


def index(request):
    results = Emaillist.objects.all().order_by("-id")
    data = {"results" : results}
    #return HttpResponse("ok")
    return render(request, "emaillist02/index.html", data)

def form(request):
    return render(request, "emaillist02/form.html")

def add(request):
    emaillist = Emaillist()
    emaillist.first_name = request.POST["fn"]
    emaillist.last_name = request.POST["ln"]
    emaillist.email = request.POST["email"]
    #가지고 온 자료들에 대해서 저장을 하기 위한 목적
    emaillist.save()
    return HttpResponseRedirect("/emaillist02")
