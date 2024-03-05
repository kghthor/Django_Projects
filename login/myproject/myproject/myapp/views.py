
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#from django.contrib.auth.hashers import make_password
#from django.core.mail import send_mail
#from myproject.settings import EMAIL_HOST_USER

@login_required
def home(request):
	return render(request,'sample.html')

def loginview(request):
    uname = request.POST['username']
    pwd = request.POST['password']
    user = authenticate(request, username=uname, password=pwd)
    if user is not None:
        login(request, user)
        return redirect('home')
    else:
        return render(request,"login.html")
        
def logout_view(request):
    logout(request)
    return redirect('login')


def sign_up(request):
        uform = UserCreationForm(request.POST)
        if request.method == "POST":
            if uform.is_valid():
                uname = uform.cleaned_data.get('username')
                pwd = uform.cleaned_data.get('password1')
                email=uform.cleaned_data.get('email')
                user1=User.objects.create_user(username=uname,password=pwd,email=email)
                user1.save()
                user = authenticate(request, username=uname, password=pwd)
                login(request,user)
                return redirect('home')
        else:
            uform = UserCreationForm()
        return render(request, 'registration/sign_up.html', {'form': uform})
    
def Resethome(request):
    return render(request,'registration/ResetPassword.html')

def resetPassword(request):
    responseDic={}
    try:
        usern = request.POST['uname']
        recepient=request.POST['email']
        pwd=request.POST['password']
        #subject="Password reset"
        try:
            user=User.objects.get(username=usern)
            if user is not None:
                user.set_password(pwd)
                user.save()
                #send_mail(subject,message, EMAIL_HOST_USER, [recepient])
                responseDic["errmsg"]="Password Reset Successfully"
                return render(request,"registration/ResetPassword.html",responseDic)
        except Exception as e:
            print(e)
            responseDic["errmsg"]="Email doesnt exist"
            return render(request,"registration/ResetPassword.html",responseDic)
        
    except Exception as e:
        print(e)
        responseDic["errmsg"]="Failed to reset password"
        return render(request,"registration/ResetPassword.html",responseDic)
