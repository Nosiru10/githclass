
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('index/', views.index, name="index")
]
