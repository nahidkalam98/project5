from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def String1(request):
    return HttpResponse('<marquee><b>This is my first String Response for the day</b></marquee>')

def String2(request):
    return HttpResponse('<marquee><b>This is the second String Response for this day</b></marquee>')

