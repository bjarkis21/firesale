import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator

from ads.forms.ads_forms import AdsForm
from user.models import UserProfile
from user.views import bank_info
#from ads.models import ads

# Create your views here.
from ads.models import Category, Advertisement

adv = [
    {'id':1, 'title':'First ad', 'price':'$100'},
    {'id':2, 'title':'Second ad', 'price':'$200'},
    {'id':3, 'title':'Third ad', 'price':'$300'},
]

def ads(request):
    if 'filterby' in request.GET:
        filterby = request.GET.get('filterby')
        category = Category.objects.get(name=filterby)
        all_ads = Advertisement.objects.filter(category=category).order_by('-creation_date')
    else:
        all_ads = Advertisement.objects.all().order_by('-creation_date')
    return render(request, 'ads.html', {
        'categories': Category.objects.all(),
        'all_ads': all_ads
    })

def get_ad_by_id(request, id):
    ad = get_object_or_404(Advertisement, pk=id)
    seller = ad.seller.userprofile
    return render(request, 'ads/single_ad.html', {
        'categories': Category.objects.all(),
        'ad': ad,
        'seller': seller
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
#def listing(request):
   # adslist = ads.objects.all()
    #paginator = Paginator(adslist)

    #page_number = request.GET.get('page')
    #page_obj = paginator.get_page(page_number)
    #return render(request, ads.html,{'page_obj': page_obj})

