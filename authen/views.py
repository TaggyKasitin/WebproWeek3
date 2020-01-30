from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse ('Hi this is aut6hentication index page')

def lec_today(request):
    return HttpResponse ('Today Lecture is ......')

def lecture(request, id):
    return HttpResponse ('This Subject is %s' % id)

def check(request):
    return HttpResponse ('Today we have 17 student in class and 3 absent')