from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_views(request):
    template_name = "auth-login.html"
    
    #verifica si el usuario esta autenticated
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        print("Entro")
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        print(username, password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            print("Error")
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

#view for logout
def logout_view(request):
    logout(request)
    return redirect('login')