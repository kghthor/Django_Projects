from django.shortcuts import render
from app2.models import reg

# Create your views here.
def view2(request):
    if request.method=='POST':
        obj=reg()
        obj.name=request.POST.get("name")
        obj.email=request.POST.get("email")
        obj.gender=request.POST.get("gender")
        obj.age=request.POST.get("age")
        obj.place=request.POST.get("place")
        obj.save()
    return render(request,"reg1.html")
def view3(request):
    obj=reg.objects.all()
    return render(request,'tab.html',{'data':obj})