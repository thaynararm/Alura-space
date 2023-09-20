from django.shortcuts import render

def login(request):
    return render(request, 'users/login.html')

def registers(request):
    return render(request, 'users/registers.html')