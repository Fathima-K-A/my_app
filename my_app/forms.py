# form

from django import forms

class Register(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(max_length=100)
    first_name=forms.CharField(max_length=50)
    last_name=forms.CharField(max_length=500)
