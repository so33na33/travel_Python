from django.contrib import auth, messages
from django.contrib.auth.models import User

from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        usname=request.POST['username']
        passwords=request.POST['password']
        user=auth.authenticate(username=usname,password=passwords)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid Login Plz Register")
            return redirect('login')
    return render(request,"login.html")
def register(request):
    if request.method=='POST':
        fname=request.POST['firstname']
        lname=request.POST['lastname']
        email=request.POST['email']
        uname=request.POST['username']
        pwd=request.POST['password']
        cpwd=request.POST['confirm password']
        if pwd==cpwd:
            if User.objects.filter(username=uname).exists():
                messages.info(request,"username already exists")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email already exists")
                return redirect('register')
            else:
                user=User.objects.create_user(username=uname,password=pwd,first_name=fname,last_name=lname,email=email)
                user.save();
                return redirect('login')
        else:
            messages.info(request,"Password Not Matching")
            return redirect('register')
    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')