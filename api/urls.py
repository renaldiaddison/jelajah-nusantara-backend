from django.shortcuts import render

from django.urls import path
from . import views


# Create your views here.
urlpatterns = [
    path('news/', views.getAllNews, name="getAllNews"),
]