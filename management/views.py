from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse ('Hi this is index')

def allstudent(request):
    return HttpResponse ('This class has .... people')

def addstd(request):
    return HttpResponse ('Add student')

def edtstd(request):
    return HttpResponse ('Edit Student')

def allsjt(request):
    return HttpResponse ('This class has .... people')

def addsjt(request):
    return HttpResponse ('Add student')

def edtsjt(request):
    return HttpResponse ('Edit Student')