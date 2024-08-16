from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout
from django.contrib.auth import get_user_model
from django.contrib import messages


def checkingNameEmail(request, email, name):
    if User.objects.filter(email=email):
        messages.error(request, 'Аккаунт для указанной электронной почты уже существует')
        return False
    
    if len(name) > 255:
        messages.error(request, 'Имя слишком длинное')
        return False
    
    if not name.isalnum():
        messages.error(request, 'Имя может состоять только из цифр и букв')
        return False
    return True

User = get_user_model()

def login(request):
    if request.POST:
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            dj_login(request, user)
            return render(request, 'profile.html')
        else:
            messages.error(request, "Bad credentials")
            return render(request, 'index.html')

    return render(request, 'login.html')

def logout(request):
    dj_logout(request)
    messages.success(request, "Logged")
    return redirect('main:index')

def registration(request):
    if request.POST:
        name = request.POST.get('name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if not checkingNameEmail(request, email, name):
            return redirect('user:registration')

        if password1 != password2:
            messages.error(request, 'Пароли не совпадают')
            return redirect('user:registration')

        user = User.objects.create_user(name=name, email=email, password=password1)
        
        user.save()
        messages.success(request, "Вы успешно зарегистрировались")

        dj_login(request, user)
        return render(request, 'index.html')
        
    return render(request, 'registration.html')

