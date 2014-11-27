from django.contrib.auth.forms import AuthenticationForm
from django.conf import settings


def add_settings(request):
    return {'settings': settings}


def login_form(request):
    return {'login_form': AuthenticationForm}