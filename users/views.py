from django.shortcuts import render
from users.forms import LoginForm, RegisterForm

def login(request):
    form = LoginForm
    return render(request, 'users/login.html', {'form': form})

def registers(request):
    form = RegisterForm
    return render(request, 'users/registers.html', {'form': form})
