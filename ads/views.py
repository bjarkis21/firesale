import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from ads.forms.ads_forms import AdsForm
from user.views import bank_info

# Create your views here.
from ads.models import Category, Advertisement

adv = [
    {'id':1, 'title':'First ad', 'price':'$100'},
    {'id':2, 'title':'Second ad', 'price':'$200'},
    {'id':3, 'title':'Third ad', 'price':'$300'},
]

def ads(request):
    return render(request, 'ads.html', {
        'categories': Category.objects.all(),
        'all_ads': Advertisement.objects.all()
    })

def get_ad_by_id(request, id):
    ad = Advertisement.objects.all().filter(pk=id)
    return render(request, 'single_ad.html', {
        'categories': Category.objects.all(),
        'ad': ad
    })

@login_required
def create_ad1(request):
    return bank_info(request, 'create-ad2')

@login_required
def create_ad2(request):
    if request.method == 'POST':
        form = AdsForm(data=request.POST)
        if form.is_valid():
            d = form.save(commit=False)
            d.seller = request.user
            d.save()
            return redirect('home')

    return render(request, 'ads/create_ad.html', {
        'form': AdsForm(),
        'categories': Category.objects.all()
    })