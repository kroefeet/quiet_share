# Settings that are unique to production go here
from .base import *  # noqa

DEBUG = TRUE

# Configure Django App for Heroku.
import django_heroku
django_heroku.settings(locals())
