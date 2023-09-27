from django.shortcuts import render, redirect
from users.forms import LoginForm, RegisterForm
from django.contrib import messages, auth
from django.contrib.auth.models import User

def login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form['login_username'].value()
            password = form['login_password'].value()

        user = auth.authenticate(
            request,
            username = username,
            password = password,
        )

        if user is not None:
            auth.login(request, user)
            messages.success(request, f'{username} logado com sucesso!')
            return redirect('index')
        
        else:
            messages.error(request, 'Usuário e/ou senha incorreto!')
            return redirect('login')

    return render(request, 'users/login.html', {'form': form})

def registers(request):

    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            if form["register_password"].value() != form["password_confirmation"].value():
                messages.error(request, 'As senhas não coferem!')
                return redirect('registers')
                
            username = form['register_username'].value()
            email = form['register_email'].value()
            password = form['register_password'].value()

            if User.objects.filter(username=username).exists():
                messages.error(request, 'Nome de usuário já cadastrado!')
                return redirect('registers')
            
            user = User.objects.create_user(
                username = username,
                email = email,
                password = password,
            )

            user.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('login')

    return render(request, 'users/registers.html', {'form': form})


