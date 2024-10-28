from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/login')

def home_views(request):
    template_name = "index.html"
    
    return render(request, template_name)