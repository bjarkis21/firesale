from django.forms import ModelForm, widgets
import django.forms as forms
from ads.functions import get_minimum_bid
from ads.models import Advertisement, BidsOn
from user.models import Checkout


class AdsForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].label = "Titill"
        self.fields['short_description'].label = "Stutt lýsing"
        self.fields['condition'].label = "Ástand"
        self.fields['category'].label = "Flokkur"
        self.fields['reserve'].label = "Lágmarksverð"
        self.fields['image'].label = "Mynd (URL)"
        self.fields['long_description'].label = "Ítarleg lýsing"
        self.fields[
            'image'].initial = 'https://t4.ftcdn.net/jpg/04/70/29/97/360_F_470299797_UD0eoVMMSUbHCcNJCdv2t8B2g1GVqYgs.jpg'

    class Meta:
        model = Advertisement
        exclude = ['id', 'seller', 'creation_date', 'buyer', 'rating', 'buy_date', 'isPaid', 'isSold', 'isActive']
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

    def __init__(self, ad, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self.ad = ad
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
        if amount < self.minimum_bid:
            raise forms.ValidationError("Boð má ekki vera lægra en lágmarksboð.")
            # self._errors['amount'] = self.error_class(['Boð má ekki vera lægra en lágmarksboð.'])
        if self.user == self.ad.seller:
            raise forms.ValidationError("Ekki er hægt að bjóða í eigin vöru.")
            # self._errors['user'] = self.error_class(['Ekki er hægt að bjóða í eigin vöru.'])
        if self.ad.isActive == False:
            raise forms.ValidationError("Þessi auglýsing er ekki lengur virk")

        return self.cleaned_data


class CheckoutForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fullname'].label = "Fullt Nafn"
        self.fields['street'].label = "Gata"
        self.fields['street_no'].label = "Húsnúmer"
        self.fields['city'].label = "Borg"
        self.fields['country'].label = "Land"
        self.fields['postcode'].label = "Póstnúmer"
        self.fields['credid_card_fullname'].label = "Nafn Korthafa"
        self.fields['credid_card_number'].label = "Kortanúmer"
        self.fields['credid_card_expiration_date'].label = "Gildistími"
        self.fields['credid_card_cvc'].label = "CVC"

    class Meta:
        model = Checkout
        exclude = ['id', 'user', 'advertisement']
        widgets = {
            'fullname': widgets.TextInput(attrs={'class': 'form-control address-info'}),
            'street': widgets.TextInput(attrs={'class': 'form-control address-info'}),
            'street_no': widgets.TextInput(attrs={'class': 'form-control address-info'}),
            'city': widgets.TextInput(attrs={'class': 'form-control address-info'}),
            'country': widgets.TextInput(attrs={'class': 'form-control address-info'}),
            'postcode': widgets.TextInput(attrs={'class': 'form-control address-info'}),
            'credid_card_fullname': widgets.TextInput(attrs={'class': 'form-control cc-info'}),
            'credid_card_number': widgets.TextInput(attrs={'class': 'form-control cc-info'}),
            'credid_card_expiration_date': widgets.TextInput(attrs={'class': 'form-control cc-info'}),
            'credid_card_cvc': widgets.TextInput(attrs={'class': 'form-control cc-info'}),
        }
