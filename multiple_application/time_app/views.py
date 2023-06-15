from django.shortcuts import render
from django.http import HttpResponse
import time

def timer(request):
    st='<h1 style="margin:auto;">now time is :'+time.strftime("%H-%M-%S")+'</h1>'
    return HttpResponse(st)

