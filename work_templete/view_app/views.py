from django.shortcuts import render
import time

# Create your views here.
def temp(request):
 
    return render(request,'base.html',context={'time':time.strftime('%H-%M-%S')})