from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


def index(request):
    data = {
        'title': "Главная страница",

    }
    return render(request,'main/index.html', data)


def about(request):
    return render(request,'main/about.html')


def contact(request):
    return render(request,'main/contact.html')


def account(request):
    return render(request,'main/account.html')


def register_request(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Регистрация прошла успешно')
            return redirect('main/index.html')
        messages.error(request, 'Ошибка! Проверьте правильность ввода данных.')
    form = NewUserForm()
    return render(request, 'main/register.html', context={'register_form': form})


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request,f'Вы заходите как {username}')
                return redirect('main/home')
            else:
                messages.error(request,'Не правильное имя или пароль')
        else:
            messages.error(request,'Не правильное имя или пароль')
    form = AuthenticationForm()
    return render(request, 'main/account.html', context={'login_form': form})


def logout_request(request):
    logout(request)
    messages.info(request,'Вы вышли из учетной записи')
    return redirect('main:home')