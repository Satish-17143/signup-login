from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        
        if password != cpassword:
            messages.error(request, "Passwords do not match")
            return redirect('/signup')
        
        try:
            user = User.objects.get(username=username)
            messages.error(request, "Username already taken")
            return redirect('/signup')
        except User.DoesNotExist:
            pass
        
        try:
            user = User.objects.get(email=email)
            messages.error(request, "Email already taken")
            return redirect('/signup')
        except User.DoesNotExist:
            pass
        
        myuser = User.objects.create_user(username, email, password)
        myuser.save()
        messages.success(request, "User created successfully. Please log in.")
        return redirect('/login')
    
    return render(request, "signup.html")

def handlelogin(request):
    if request.method == "POST":
        username=request.POST.get("username")
        password = request.POST.get('password')
        myuser=authenticate(username=username,password=password)
        if myuser is not None:
            login(request,myuser)
            messages.success(request,'Login Successfully')
            return HttpResponse("LOGIN Succesfull")
        else:
            messages.error(request,'Invalid Credentials')
            return redirect('/login')
            
        
    return render(request,"login.html")