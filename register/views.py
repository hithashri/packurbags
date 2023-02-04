from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from store.models import *
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            Customer.objects.create(
                user = user,
                name = user.username,
                email = user.email
            )
        return redirect("/login")
    else:
        form = RegisterForm()  

    return render(request, "register/register.html", {'form':form})