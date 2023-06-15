from django.shortcuts import render
from django.http import HttpResponse
import time

# Create your views here.

def msg(request):
    if (time.strftime('%H') < '12'):
        return HttpResponse('<h1>good morning ,sir </h1>')
    elif time.strftime('%H')<'16':
        return HttpResponse('<h1>good afternoon,sir </h1>')
    elif time.strftime('%H')<'20':
        return HttpResponse('<h1>good evening,sir </h1>')
    else:
        return HttpResponse('<h1>good night,sir </h1>')


   
        
    
