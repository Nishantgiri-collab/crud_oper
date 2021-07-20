from django import forms
from .models import Product
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class Productforms(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class Signupform(UserCreationForm):
    class Meta:
        model = User
        fields =['username','first_name', 'last_name', 'email']
