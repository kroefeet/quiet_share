from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django import forms
from django.forms import ModelForm, PasswordInput

from apps.accounts.forms import UserEditForm, SignupForm
from apps.accounts.models import User
from apps.core.models import FilePost

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'password']

def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('/')
    else:
        form = AuthenticationForm()

    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

def log_out(request):
    logout(request)
    return redirect('/')


def save(self, *args, **kwargs):
    self.crew_password = make_password(self.crew_password)
    super(Crew, self).save(*args, **kwargs)

def sign_up(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = forms.CharField(widget=forms.PasswordInput)
            user.set_password(form.cleaned_data['password'])
            user.save()

            # Log-in the user right away
            messages.success(request, 'Account created successfully. Welcome!')
            login(request, user)
            return redirect('/')
    else:
        form = SignupForm()

    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)

# def logout_view(request):
#     logout(request)
#     messages.success(request, 'Logged out.')
#     return redirect('home')
