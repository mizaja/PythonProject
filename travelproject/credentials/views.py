from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        name=request.POST['userid']
        passw=request.POST['pwd']
        user=auth.authenticate(username=name,password=passw)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"not valid")
            return redirect('login')


    return render(request,"login.html")
def registration(request):
    if request.method=='POST':
        uname = request.POST['Uname']
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        pass0 = request.POST['Pass']
        pass1 = request.POST['Pass1']
        email = request.POST['email']
        if pass0==pass1:
            if User.objects.filter(username=uname).exists():
                messages.info(request,"username exist")
                return redirect('registration')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email exist")
                return redirect('registration')
            else:
             user=User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=email,password=pass0)
             user.save();
             print("saved")
             return redirect('login')
        else:
            messages.info(request,"not matching")
            return redirect('registration')
        return redirect('/')
    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')