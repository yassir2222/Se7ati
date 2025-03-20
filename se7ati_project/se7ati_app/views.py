from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import PatientSignUpForm , DoctorSignUpForm, LoginForm
from .models import Patient, Doctor, User 
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, World!")

def patient_register(request):
    if request.method == 'POST':
        form = PatientSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login') 
    else:
        form = PatientSignUpForm()
    return render(request, 'registration/register.html', {'form': form})


def doctor_register(request):
    if request.method == 'POST':
        form = DoctorSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')  
        form = DoctorSignUpForm()
    return render(request, 'registration/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.is_patient:
                return redirect('login')
            else:
                return redirect('login')
        else:
            print(form.errors)
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.user_type == 'patient':
                    return redirect('home')
                elif user.user_type == 'doctor':
                    return redirect('home')
                else:
                    return redirect('home')  # Fallback
        else:
            return render(request, 'registration/login.html', {'form': form})
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
   # logout(request)
    return redirect('login') 


