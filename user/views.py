from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404

from ads.functions import get_max_bid
from ads.models import Category, Advertisement, BidsOn
from user.forms.profile_forms import ProfileForm, BankInfoForm, CustomUserForm
from user.models import UserProfile


# Create your views here.


def register(request):
    if request.method == 'POST':
        form = CustomUserForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            profile = UserProfile()
            profile.user = user
            profile.save()
            return redirect('login')
    return render(request, 'user/register.html', {
        'form': CustomUserForm(),
        'categories': Category.objects.all()
    })


@login_required
def profile(request):
    profile = UserProfile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    return render(request, 'user/profile.html', {
        'form': ProfileForm(instance=profile),
        'categories': Category.objects.all()
    })


@login_required
def bank_info(request, redirect_url='profile'):
    profile = UserProfile.objects.filter(user=request.user).first()
    if profile == None:
        profile = UserProfile()
        # profile.save(commit=False)
        profile.user = request.user
        profile.save()
    if request.method == 'POST':
        form = BankInfoForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save()
            return redirect(redirect_url)
    return render(request, 'user/bank_info.html', {
        'form': BankInfoForm(instance=profile),
        'categories': Category.objects.all()
    })


@login_required
def myproducts(request, redirect_url='myproducts'):
    #ad = get_object_or_404(Advertisement, pk=id)
    seller = request.user
    user_ads = Advertisement.objects.filter(seller=seller).order_by('-creation_date')
    for ad in user_ads:
        ad.max_bid = get_max_bid(ad)
    return render(request, 'user/myproducts.html', {
        'categories': Category.objects.all(),
        'user_ads': user_ads
    })


def mybids(request, redirect_url='mybids'):
    bidder = request.user
    bidder_ads = Advertisement.objects.filter(bidson__user=bidder).distinct()
    for ad in bidder_ads:
        ad.max_bid = get_max_bid(ad)
        ad.max_user_bid = get_max_bid(ad, bidder)
    return render(request,'user/mybids.html', {
        'categories': Category.objects.all(),
        'user_ads': bidder_ads,
        'bidder': bidder
    })


def salehistory(request, redirect_url='salehistory'):
    return render(request,'user/salehistory.html', {
        'categories': Category.objects.all()
    })


def purchases(request, redirect_url='purchases'):
    return render(request,'user/purchases.html', {
        'categories': Category.objects.all()
    })


def notifications(request, redirect_url='notifications'):
    return render(request,'user/notifications.html', {
        'categories': Category.objects.all()
    })
