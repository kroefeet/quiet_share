from django.shortcuts import render, redirect
from django import forms
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from py3wetransfer import Py3WeTransfer
import os
wetransfer_api_key = os.environ["WeTransfer_API_KEY"]
from .models import FilePost

# Two example views. Change or delete as necessary.

class QuietShareForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    username = forms.CharField(max_length=30)
    filename = forms.FileField(label = "Select a file")

# Two example views. Change or delete as necessary.
def home(request):

    context = {
        'example_context_variable': 'Change me.',
    }

    return render(request, 'pages/index.html', context)

def file(request):
    if request.method == 'POST':
                # Create a form instance and populate it with data from the request
        form = QuietShareForm(request.POST)
        x = Py3WeTransfer(wetransfer_api_key)

#        if form.is_valid():
        filename=request.POST['filename']
        text=request.POST['text']
        link = x.upload_file(filename, text)

        filepost = FilePost.objects.create(
            username=request.POST['username'],
            text=text,
            link = link,
        )

            # As soon as our new user is created, we make this user be
            # instantly "logged in"
            #auth.login(request, user)
        return redirect('/')

    else:
        # if a GET we'll create a blank form
        form = QuietShareForm()

    context = {
        'form': form,
    }
    return render(request, 'pages/file0.html', context)
