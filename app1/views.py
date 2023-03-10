from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def karishma(request):
    return HttpResponse('<marquee><h1>she is my friend</h1></marquee>')

def aliaa(request):
    return HttpResponse('<marquee><h1>good girl</h1></marquee>')
