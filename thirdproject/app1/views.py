from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def new1(request):
    return HttpResponse('<h1>first app first fuction</h1>')
def new2(request):
    return HttpResponse('<h1>first app second fuction</h1>')
def view1(request):
    return render(request,'new.html')
def view2(request):
    return render(request,'reg.html')