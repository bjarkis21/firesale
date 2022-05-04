from django.forms import ModelForm, widgets

from ads.models import Advertisement


class AdsForm(ModelForm):
    class Meta:
        model = Advertisement
        exclude = ['id', 'seller', 'creation_date', 'buyer', 'rating', 'buy_date', 'isPaid', 'isSold']
        widgets = {
            'title': widgets.TextInput(attrs={'class': 'form-control'}),
            'short_description': widgets.TextInput(attrs={'class': 'form-control'}),
            'long_description': widgets.TextInput(attrs={'class': 'form-control'}),
            'condition': widgets.TextInput(attrs={'class': 'form-control'}),
            'reserve': widgets.NumberInput(attrs={'class': 'form-control'}),
            'image': widgets.TextInput(attrs={'class': 'form-control'}),
        }