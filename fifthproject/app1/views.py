from django.shortcuts import redirect, render
from app1.models import doctor

# Create your views here.
def doc1(request):
    if request.method=='POST':
        obj=doctor()
        obj.name=request.POST.get("name")
        obj.email=request.POST.get("email")
        obj.gender=request.POST.get("gender")
        obj.age=request.POST.get("age")
        obj.place=request.POST.get("place")
        obj.save()
        return redirect("docview")
    return render(request,"docreg.html")
def docview(request):
    obj=doctor.objects.all()
    return render(request,'docview.html',{'data':obj})
def doc2(request,pk):
    obj=doctor.objects.get(id=pk)
    if request.method=='POST':
        obj=doctor.objects.get(id=pk)
        obj.name=request.POST.get("name")
        obj.email=request.POST.get("email")
        obj.gender=request.POST.get("gender")
        obj.age=request.POST.get("age")
        obj.place=request.POST.get("place")
        obj.save()
        return redirect("docview")
    return render(request,"update1.html",{'data':obj})
def delete(request,pk):
    obj=doctor.objects.get(id=pk)
    obj.delete()
    return docview(request)