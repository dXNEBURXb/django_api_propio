from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

#view for Login
def login_views(request):
    template_name = "auth-login.html"
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, template_name, {'error': 'Credenciales inválidas'})
    return render(request, template_name)

#view for Register
def register_view(request):
    template_name = "auth-register.html"
    return render(request, template_name)

#view for Forgot The Password
def forgot_view(request):
    template_name = "auth-forgot-password.html"
    return render(request, template_name)
