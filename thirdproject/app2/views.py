from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def new1(request):
    return HttpResponse('<h1>second app first fuction</h1>')
def new2(request):
    return HttpResponse('<h1>second app second fuction</h1>')
def view1(request):
    return render(request,"abt.html",{'name':'King'})
def view2(request):
    return render(request,'design.html')