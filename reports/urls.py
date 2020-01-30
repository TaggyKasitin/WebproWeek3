from django.contrib import admin
from django.urls import path
from reports import views

urlpatterns = [
    path('', views.index),
    path('dashboard/', views.dashboard),
    path('classattend/', views.classattend)
]
