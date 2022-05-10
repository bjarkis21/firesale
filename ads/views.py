import datetime
from django.http import JsonResponse

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator

from ads.forms.ads_forms import AdsForm, BidForm,CheckoutForm
from user.models import UserProfile
from user.views import bank_info
from ads.models import BidsOn
from django.db.models import Max
from ads.functions import get_max_bid

# Create your views here.
from ads.models import Category, Advertisement

adv = [
    {'id': 1, 'title': 'First ad', 'price': '$100'},
    {'id': 2, 'title': 'Second ad', 'price': '$200'},
    {'id': 3, 'title': 'Third ad', 'price': '$300'},
]


def ads(request):
    filterby = None
    if 'filterby' in request.GET and 'search_filter' in request.GET:
        filterby = request.GET.get('filterby')
        search_filter = request.GET.get('search_filter')
        category = Category.objects.get(name=filterby)
        all_ads = Advertisement.objects.filter(category=category, title__icontains=search_filter, isActive=True).order_by('-creation_date')
    elif 'filterby' in request.GET:
        filterby = request.GET.get('filterby')
        category = Category.objects.get(name=filterby)
        all_ads = Advertisement.objects.filter(category=category, isActive=True).order_by('-creation_date')
    elif 'search_filter' in request.GET:
        search_filter = request.GET.get('search_filter')
        all_ads = Advertisement.objects.filter(title__icontains=search_filter, isActive=True).order_by('-creation_date')
    else:
        all_ads = Advertisement.objects.filter(isActive=True).order_by('-creation_date')

    for ad in all_ads:
        ad.max_bid = get_max_bid(ad)

    return render(request, 'ads.html', {
        'categories': Category.objects.all(),
        'all_ads': all_ads,
        'filterby': filterby
    })


def get_ad_by_id(request, id):
    ad = get_object_or_404(Advertisement, pk=id)
    method = request.method
    seller = ad.seller.userprofile
    form = BidForm(ad=ad, user=request.user)
    if request.method == 'POST':
        form = BidForm(ad=ad, user=request.user, data=request.POST)
        if form.is_valid():
            bid = form.save(commit=False)
            bid.user = request.user
            bid.advertisement = ad
            bid.save()
            return redirect(f'/ads/{id}')
        else:
            print(form.errors)

    ad.max_bid = get_max_bid(ad)

    return render(request, 'ads/single_ad.html', {
        'categories': Category.objects.all(),
        'ad': ad,
        'seller': seller,
        'form': form
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


@login_required
def stop_ad(request, id):
    ad = get_object_or_404(Advertisement, pk=id)
    if request.user == ad.seller:
        ad.isActive = False
        ad.save()
    return redirect('myproducts')


@login_required
def confirm_bid(request, id):
    ad = get_object_or_404(Advertisement, pk=id)
    max_bid = BidsOn.objects.filter(advertisement=ad).aggregate(Max('amount'))['amount__max']
    max_bidder = BidsOn.objects.get(advertisement=ad, amount=max_bid).user
    if ad.seller == request.user and ad.isActive and not ad.isSold and not ad.isPaid:
        ad.isActive = False
        ad.isSold = True
        ad.buyer = max_bidder
        ad.save()

    return redirect('myproducts')


@login_required
def checkout(request,id):
    if request.method == 'POST':
        form = CheckoutForm(data=request.POST)
        if form.is_valid():
            d = form.save(commit=False)
            d.seller = request.user
            d.save()
            return redirect('home')

    return render(request, 'ads/checkout.html', {
        'form': CheckoutForm(),
        'categories': Category.objects.all()
    })




# def listing(request):
# adslist = ads.objects.all()
# paginator = Paginator(adslist)

# page_number = request.GET.get('page')
# page_obj = paginator.get_page(page_number)
# return render(request, ads.html,{'page_obj': page_obj})
