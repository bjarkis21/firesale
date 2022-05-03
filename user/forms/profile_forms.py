from django.forms import ModelForm, widgets

from user.models import UserProfile


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
