from django import forms
from .models import *

class BasicInfoForm(forms.Form):
    '''
    BasicInfo Model Form
    '''
    username = forms.CharField(required=True)
    name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone = forms.IntegerField(min_value=10, max_value=10)
    password = forms.CharField(required=True, widget=forms.PasswordInput())
    food = forms.CharField(required=True)
