from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterForm

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')  # Redirect after login
    else:
        form = RegisterForm()
    return render(request, 'FitFair/register.html', {'form': form})

def dashboard(request):
    return render(request, 'dashboard.html')

def login(request):
    return render(request, 'login.html')





# Create your views here.
