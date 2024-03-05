from django.shortcuts import redirect, render
from libadmin.models import reg
# Create your views here.
def doc1(request):
    if request.method=='POST':
        obj=reg()
        obj.name=request.POST.get("name")
        obj.email=request.POST.get("email")
        obj.author=request.POST.get("author")
        obj.price=request.POST.get("price")
        obj.discription=request.POST.get("discription")
        obj.save()
        return redirect('viewmsg')
    return render(request,"reg.html")
def docview(request):
    obj=reg.objects.all()
    return render(request,'regview.html',{'data':obj})
def stamod(request):
    return render(request,'index.html')
def serv(request):
    return render(request,'service.html')
def abt(request):
    return render(request,'about.html')
def tem(request):
    return render(request,'team.html')
def wh(request):
    return render(request,'why.html')
    
    