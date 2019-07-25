from django.shortcuts import render, redirect
from django import forms
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

from py3wetransfer import Py3WeTransfer
import os
wetransfer_api_key = os.environ["WeTransfer_API_KEY"]
from .models import FilePost
from apps.accounts.models import User
import datetime


# Two example views. Change or delete as necessary.

class QuietShareForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    recipient_username = forms.CharField(max_length=30)
    filename = forms.FileField(label = "Select a file", required=False)

# Two example views. Change or delete as necessary.
def home(request):
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request
        form = QuietShareForm(request.POST)
        x = Py3WeTransfer(wetransfer_api_key)

        filename=request.POST['filename']
        text=request.POST['text']
        if not filename:
            link = ''
        else:
            link = x.upload_file(filename, text)
        dt_now = datetime.datetime.now()

        filepost = FilePost.objects.create(
            username=request.POST['username'],
            text=text,
            link = link,
            expiry_date = dt_now + datetime.timedelta(days=7),
        )

        return redirect('/accounts/login')

    else:
        # if a GET we'll create a blank form
        form = QuietShareForm()

    context = {
        'form': form,
    }

    return render(request, 'pages/index.html', context)

@login_required
def user_page(request, username):
    check = str(request.user)
    if check == username:
        user = User.objects.get(username=username)
        links = FilePost.objects.filter(username=user)

        context = {
            'user': user,
            'links': links,
        }
        return render(request, 'pages/user_page.html', context)
    else:
        return redirect('/')


@login_required
def delete_profile(request, username):
    check = str(request.user)
    if check == username:
        user = User.objects.get(username=username)
        user.delete()

    return redirect('/')
