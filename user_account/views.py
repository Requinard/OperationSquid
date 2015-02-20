from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *


# Create your views here.
class LoginView(View):
    def get(self, request):
        context = {}

        context['login-form'] = LoginForm()
        return render(request, "user_account/login.html", context)

    def post(self, request):
        context = {}

        form = LoginForm(request.POST)

        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])

            if user is not None:
                # Check if the password was verified
                if user.is_active:
                    login(request, user)
                    messages.success(request, "Login successful")
                    return redirect("events:index")
                else:
                    context['error'] = "This user has been banned!"
            else:
                context['error'] = "The username or password was incorrect"

        context['login-form'] = form

        return render(request, "user_account/login.html", context)

class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, "Logout successful")
        return redirect("user:login")

class IndexView(View):
    def get(self, request):
        return render(request, "base.html", {})

class UserPageView(View):
    def get(self, request, username):
        return render(request, "base.html", {})
