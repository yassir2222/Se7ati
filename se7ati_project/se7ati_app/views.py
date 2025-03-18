from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout

def home(request):
    return HttpResponse("Hello, World!")

def register_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        print(username,password)
        confirm_password = request.POST['confirm-password']
        if password == confirm_password:
            try:
                user = User.objects.create_user(username=username,password=password,email=email)
                user.save()
                login(request,user)
                return redirect('login')
            
            except:
                messages.error(request, 'An error occurred during registration.')
    else:
        messages.error(request,"password do no match")        
 
    return render(request, "registration/register.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, "registration/login.html")

def logout_view(request):
    logout(request)
    return redirect('login')        