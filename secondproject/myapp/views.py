from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def party(request):
    return HttpResponse('<h1>MY app</h1>')
def part(request):
    return HttpResponse('<h1>MY app first page</h1>')