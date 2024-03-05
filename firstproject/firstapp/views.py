from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def display(request):
    return HttpResponse('<h1>Hello world</h1>')
def add(request):
    return HttpResponse('<p>Hey bud buddy i can see you</p>')
def sub(request):
    return HttpResponse('<h1>We are heroes</h1>')
def displa(request):
    return HttpResponse('<h1>Hello king</h1>')
def dispy(request):
    return HttpResponse('<h1>Hello bull</h1>')