# authentication/views.py
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.views import View # import des fonctions login et authenticate

def logout_user(request):
    
    logout(request)
    return redirect('login')