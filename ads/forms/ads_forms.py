from django.forms import ModelForm, widgets
import django.forms as forms
from ads.functions import get_minimum_bid
from ads.models import Advertisement, BidsOn


class AdsForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].label = "Titill"
        self.fields['short_description'].label = "Stutt lýsing"
        self.fields['condition'].label = "Ástand"
        self.fields['category'].label = "Flokkur"
        self.fields['reserve'].label = "Lágmark"
        self.fields['image'].label = "Mynd (URL)"
        self.fields['long_description'].label = "Ýtarleg lýsing"

    class Meta:
        model = Advertisement
        exclude = ['id', 'seller', 'creation_date', 'buyer', 'rating', 'buy_date', 'isPaid', 'isSold']
        widgets = {
            'title': widgets.TextInput(attrs={'class': 'form-control'}),
            'short_description': widgets.TextInput(attrs={'class': 'form-control'}),
            'condition': widgets.TextInput(attrs={'class': 'form-control'}),
            'category': widgets.Select(attrs={'class': 'form-control'}),
            'reserve': widgets.NumberInput(attrs={'class': 'form-control'}),
            'image': widgets.TextInput(attrs={'class': 'form-control'}),
            'long_description': widgets.Textarea(attrs={'class': 'form-control', 'rows': '5', 'cols': '21'}),
        }


class BidForm(ModelForm):

    def __init__(self, ad, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['amount'].label = "Bjóða í vöru"
        self.minimum_bid = get_minimum_bid(ad)
        self.fields['amount'].widget.attrs['placeholder'] = f"Lágmarksboð: {self.minimum_bid} kr."

    class Meta:
        model = BidsOn
        exclude = {'id', 'user', 'advertisement'}
        widgets = {
            'amount': widgets.NumberInput(attrs={'class': 'form-control'})
        }

    def clean(self):
        super(BidForm, self).clean()
        amount = self.cleaned_data.get('amount')
        if amount <= self.minimum_bid:
            raise forms.ValidationError("Boð má ekki vera lægra en lágmarksboð.")
            #self._errors['amount'] = self.error_class(['Boð má ekki vera lægra en lágmarksboð'])

        return self.cleaned_data
