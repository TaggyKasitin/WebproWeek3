from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse ('Report Index')

def dashboard(request):
    return HttpResponse ('Today subject is .....')

def classattend(request):
    return HttpResponse ('This subject has .... attend and .... absent')