from django.urls import path
from time_app import views

urlpatterns = [
   
    path('', views.timer,name="timer"),
]