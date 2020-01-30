from django.contrib import admin
from django.urls import path
from management import views

urlpatterns = [
    path('', views.index),
    path('allstudent/', views.allstudent),
    path('addstd/', views.addstd),
    path('edtstd/', views.edtstd),
    path('allsjt/', views.allsjt),
    path('addsjt/', views.addsjt),
    path('edtsjt/', views.edtsjt)
]
