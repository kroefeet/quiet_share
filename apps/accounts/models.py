import hashlib

from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom User class which extends built-in User. Presently, just adds a "bio"
# and a gravatar method. Feel free to add your own new fields here!

class User(AbstractUser):

    bio = models.TextField()

    def gravatar(self, size=None):
        GRAVATAR_URL = 'https://gravatar.com/avatar/%s?d=identicon%s'
        email = str(self.email).strip().lower()
        digest = hashlib.md5(email.encode('utf-8')).hexdigest()

        if size:
            size_str = '&s=%i' % size
        else:
            size_str = ''

        return GRAVATAR_URL % (digest, size_str)



class Meta:
    model = User
    fields = ["username", "password"]

def __init__(self, *args, **kwargs):
    # first call the 'real' __init__()
    super(LoginForm, self).__init__(*args, **kwargs)
    # then do extra stuff:
    self.fields['username'].help_text = ''
    self.fields['password'].widget = forms.PasswordInput(attrs={'placeholder': ''})
    self.fields['password'].widget.attrs['class'] = 'form-control'
