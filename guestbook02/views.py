from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from guestbook02.models import Guestbook


def index(request):

    results = Guestbook.objects.all().order_by("-regdate")
    data = {"results": results}
    return render(request, "guestbook02/index.html", data)

def add(request):
    guestbook = Guestbook()
    guestbook.name = request.POST["name"]
    guestbook.password = request.POST["password"]
    guestbook.message = request.POST["message"]
    guestbook.save()

    return HttpResponseRedirect("/guestbook02")

def deleteform(request):
    return render(request, "guestbook02/deleteform.html")

def delete(request):
    guestbook = Guestbook.objects.filter(id=request.POST["id"], password=request.POST["password"])
    guestbook.delete()
    return render(request, "guestbook02")
