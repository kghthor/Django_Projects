from django.shortcuts import redirect, render
from app2.models import patient

# Create your views here.
def pat1(request):
    if request.method=='POST':
        obj=patient()
        obj.name=request.POST.get("name")
        obj.email=request.POST.get("email")
        obj.gender=request.POST.get("gender")
        obj.age=request.POST.get("age")
        obj.place=request.POST.get("place")
        obj.save()
    return render(request,"patreg.html")
def patview(request):
    obj=patient.objects.all()
    return render(request,'patview.html',{'data1':obj})
def doc2(request,pk):
    obj=patient.objects.get(id=pk)
    if request.method=='POST':
        obj=patient.objects.get(id=pk)
        obj.name=request.POST.get("name")
        obj.email=request.POST.get("email")
        obj.gender=request.POST.get("gender")
        obj.age=request.POST.get("age")
        obj.place=request.POST.get("place")
        obj.save()
        return redirect("patient")
    return render(request,"update1.html",{'data1':obj})
def delete(request,pk):
    obj=patient.objects.get(id=pk)
    obj.delete()
    return patview(request)