from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def greeting(request):
    return HttpResponse('<h1>Good Morning</h1>')
def greetin(request):
    return HttpResponse('<h1>Good Mornin</h1>')
def greeti(request):
    return HttpResponse('<h1>Good Morni</h1>')
def greet(request):
    return HttpResponse('<h1>Good Morn</h1>')  
