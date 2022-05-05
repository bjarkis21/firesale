from django.forms import ModelForm, widgets, EmailField
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from user.models import UserProfile

class CustomUserForm(UserCreationForm):
    email = EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['id', 'user', 'ssn', 'bank', 'hb', 'account_no', 'address', 'rating']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'phone': widgets.TextInput(attrs={'class': 'form-control'}),
            'gender': widgets.Select(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            'profile_image': widgets.TextInput(attrs={'class': 'form-control'})
        }


class BankInfoForm(ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['id', 'user', 'name', 'phone', 'rating', 'gender', 'description', 'address', 'profile_image']
        widgets = {
            'ssn': widgets.TextInput(attrs={'class': 'form-control'}),
            'bank': widgets.TextInput(attrs={'class': 'form-control'}),
            'hb': widgets.TextInput(attrs={'class': 'form-control'}),
            'account_no': widgets.TextInput(attrs={'class': 'form-control'})
        }
