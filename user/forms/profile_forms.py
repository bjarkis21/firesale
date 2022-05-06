from django.forms import ModelForm, widgets, EmailField
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from user.models import UserProfile

class CustomUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].label = "Netfang"
        self.fields['username'].label = "Notandanafn"
        self.fields['password1'].label = "Lykilorð"
        self.fields['password2'].label = "Staðfesta lykilorð"

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = "Nafn"
        self.fields['phone'].label = "Símanúmer"
        self.fields['gender'].label = "Kyn"
        self.fields['description'].label = "Lýsing"
        self.fields['profile_image'].label = "Prófílmynd"


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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['ssn'].label = "Kennitala"
        self.fields['bank'].label = "Banki"
        self.fields['hb'].label = "Höfuðbók"
        self.fields['account_no'].label = "Reikningsnúmer"

    class Meta:
        model = UserProfile
        exclude = ['id', 'user', 'name', 'phone', 'rating', 'gender', 'description', 'address', 'profile_image']
        widgets = {
            'ssn': widgets.TextInput(attrs={'class': 'form-control'}),
            'bank': widgets.TextInput(attrs={'class': 'form-control'}),
            'hb': widgets.TextInput(attrs={'class': 'form-control'}),
            'account_no': widgets.TextInput(attrs={'class': 'form-control'})
        }
