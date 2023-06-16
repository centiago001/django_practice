from django.contrib import admin
from django.urls import path,include
from LandingPage import views


urlpatterns = [
    path('',views.index),
    path('contact_us',include('contact_us.urls'))
    ]