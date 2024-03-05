from django.shortcuts import render
from django.http import HttpResponse
from .models import customer
from .forms import customerform
# Create your views here.
def index(request):
    custform=customerform()
    return render(request,"index.html",{"form":custform})
def view1(request):
    return render(request,"")