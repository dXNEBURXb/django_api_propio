from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

# Create your views here.
def login_views(request):
    template_name = "auth-login.html"

    #verifica si el usuario esta autenticado
    if request.user.is_authenticated and request.user.is_active:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        elif  request.user.is_active:
            messages.error(request, 'El usuario no esta activo')        
        else:
            messages.error(request, 'Usuario inactivo')        
    return render(request, template_name)

#view for Register
def register_view(request):
    template_name = "auth-register.html"
    if request.method =='POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']
        
        print(username)
        print(email)
        print(password)
        print(password_confirmation)
        if password != password_confirmation:
            messages.error(request, 'Las contraseñas no coinciden')
            return render(request, template_name)
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'El usuario ya existe')
            return render(request, template_name)
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'El correo que ingreso ya existe')
            return render(request, template_name)
            
        
        user = User(
            username=username,
            email=email,
            password=make_password(password),
            is_active = 0
        )
        user.save()
        messages.success(request, 'Cuenta creada correctamente')
    return render(request, template_name)

#view for Forgot The Password
def forgot_view(request):
    template_name = "auth-forgot-password.html"
    return render(request, template_name)

#view for logout
def logout_view(request):
    logout(request)
    return redirect('login')