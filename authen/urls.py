from django.contrib import admin
from django.urls import path
from authen import views

urlpatterns = [
    path('', views.index),
    path('lec_today/', views.lec_today),
    path('lecture/<int:id>/', views.lecture),
    path('check/', views.check)
]
