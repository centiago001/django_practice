
from django.urls import path,include
from greeting import views

urlpatterns = [
    
    path('',views.msg,name="msg")
]
