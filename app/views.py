from django.shortcuts import render, redirect
from .forms import Register
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import login, logout, update_session_auth_hash, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.


def home(req):
    return render(req, 'home.html')


def register(req):
    if req.method == 'POST':
        form = Register(req.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('homepage')
    else:
        form = Register()
    return render(req, 'signup.html', {'form': form})


def user_login(req):
    if req.method == "POST":
        form = AuthenticationForm(req, req.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username=user_name, password=user_pass)
            if user is not None:
                login(req, user)
                messages.success(req, 'Logged In Successfully')
                return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(req, 'signup.html', {'form': form})


@login_required
def user_logout(req):
    logout(req)
    messages.success(req, 'Logged Out Successfully')
    return redirect('homepage')


@login_required
def profile(req):
    return render(req, 'profile.html')


@login_required
def pass_with(req):
    if req.method == 'POST':
        form = PasswordChangeForm(req.user, req.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            update_session_auth_hash(req, form.user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(req.user)
    return render(req, 'passchange.html', {'form': form})


@login_required
def pass_without(req):
    if req.method == 'POST':
        form = SetPasswordForm(req.user, req.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            update_session_auth_hash(req, form.user)
            return redirect('profile')
    else:
        form = SetPasswordForm(req.user)
    return render(req, 'passchange.html', {'form': form})
