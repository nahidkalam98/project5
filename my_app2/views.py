from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def String3(request):
    return HttpResponse("<i>This is the third string response of Thursday</i>")

def String4(request):
    return HttpResponse("<marquee><i>This is the fourth string response of Today</i></marquee>")
