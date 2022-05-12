from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from ads.forms.ads_forms import AdsForm, BidForm, CheckoutForm
from user.models import Messages
from user.views import bank_info
from ads.models import BidsOn
from django.db.models import Max
from ads.functions import get_max_bid

# Create your views here.
from ads.models import Category, Advertisement

adv = [
    {'id': 1, 'title': 'First ad', 'price': '$100'},
    {'id': 2, 'title': 'Second ad', 'price': '$200'},
    {'id': 3, 'title': 'Third ad', 'price': '$300'}
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

    try:
        isNewMessage = request.user.userprofile.isNewMessage
    except AttributeError:
        isNewMessage = False

    return render(request, 'ads.html', {
        'categories': Category.objects.all(),
        'all_ads': all_ads,
        'filterby': filterby,
        'isNewMessage': isNewMessage
    })


def get_ad_by_id(request, id):
    ad = get_object_or_404(Advertisement, pk=id)
    ad_cat = ad.category
    related_ads = Advertisement.objects.filter(category=ad_cat).exclude(ad).order_by('-creation_date')[:2]
    seller = ad.seller.userprofile
    form = BidForm(ad=ad, user=request.user)
    if request.method == 'POST' and request.user.is_authenticated:
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
        'form': form,
        'related_ads': related_ads
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

        max_bidder.userprofile.isNewMessage = True
        max_bidder.userprofile.save()

        message = Messages()
        message.user = max_bidder
        message.message = f"Tilboð þitt í \"{ad.title}\" hefur verið samþykkt. Farðu í \"Mín boð\" til að ljúka greiðslu."
        message.save()

        send_mail("Ný skilaboð á Firesale",
                  f"Tilboð þitt í \"{ad.title}\" hefur verið samþykkt. Farðu í \"Mín boð\" til að ljúka greiðslu.",
                  "firesale.is.the.best@gmail.com",
                  [max_bidder.email],
                  fail_silently=False)

    return redirect('myproducts')


@login_required
def checkout(request, id):
    ad = get_object_or_404(Advertisement, pk=id)
    if ad.buyer != request.user:
        return redirect('home')
    if request.method == 'POST':
        form = CheckoutForm(data=request.POST)
        if form.is_valid():
            d = form.save(commit=False)
            d.user = request.user
            d.advertisement = ad
            d.save()
            ad.isPaid = True
            ad.save()

            rejected_bidders = BidsOn.objects.filter(advertisement=ad).exclude(user=ad.buyer).distinct('user')
            for bid in rejected_bidders:
                bidder = bid.user
                message = Messages()
                message.user = bidder
                message.message = f"Tilboð þitt í \"{ad.title}\" hefur verið hafnað."
                message.save()
                bidder.userprofile.isNewMessage = True
                bidder.userprofile.save()

            send_mail("Ný skilaboð á Firesale",
                      f"Tilboð þitt í \"{ad.title}\" hefur verið hafnað.",
                      "firesale.is.the.best@gmail.com",
                      [bid.user.email for bid in rejected_bidders],
                      fail_silently=False)

            return redirect('mybids')
    ad.max_bid = get_max_bid(ad)
    return render(request, 'ads/checkout.html', {
        'form': CheckoutForm(),
        'categories': Category.objects.all(),
        'ad': ad
    })


@login_required
def stop_bid(request, id):
    bid = get_object_or_404(Advertisement, pk=id)
    if request.user == bid.buyer:
        bid.isActive = False
        bid.save()
    return redirect('mybids')


# def listing(request):
# adslist = ads.objects.all()
# paginator = Paginator(adslist)

# page_number = request.GET.get('page')
# page_obj = paginator.get_page(page_number)
# return render(request, ads.html,{'page_obj': page_obj})
