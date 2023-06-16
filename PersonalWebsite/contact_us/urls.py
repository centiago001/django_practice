from django.contrib import admin
from django.urls import path,include
from contact_us import views


urlpatterns = [
    path('',views.submits),
]
