from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
# Create your views here.

def index(request): 
    if request.user.is_authenticated:  return redirect("/home")
    return redirect("/login")

def login_view(request): 
    if request.user.is_authenticated: return redirect("/home") 
    elif request.method == "POST":
        form = AuthenticationForm(data = request.POST)
        if(form.is_valid()):
            user = form.get_user()
            login(request, user)
            return redirect("/home")
    else: 
        form = AuthenticationForm()
    return render(request, "main/page-login.html", {"login_form" : form});

def register_view(request): 
    if request.user.is_authenticated: return redirect("/home")
    elif request.method == "POST": 
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            if 'next' in request.POST: 
                return redirect(request.POST.next)
            return redirect("")
    else: 
        form = RegistrationForm()
    return render(request, "main/page-register.html", {"register_form" : form}) # temp

def logout_view(request):
    if request.method=="POST":
        logout(request)
    return redirect("/login")

@login_required(login_url = "/login")
def home(request):
    return render(request, "main/blank.html")

