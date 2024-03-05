from django.shortcuts import render
from app1.models import employe
# Create your views here.
def view1(request):
    if request.method=='POST':
        obj=employe()
        obj.name=request.POST.get("name")
        obj.email=request.POST.get("email")
        obj.save()
    return render(request,"reg.html")