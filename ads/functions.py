from django.db.models import Max

from ads.models import BidsOn, Advertisement


def get_max_bid(ad, user=None):
    """Return maximum current bid on a single ad"""
    if user:
        max_bid_dict = BidsOn.objects.filter(advertisement=ad, user=user).aggregate(Max('amount'))
    else:
        max_bid_dict = BidsOn.objects.filter(advertisement=ad).aggregate(Max('amount'))
    if max_bid_dict is None:
        max_bid = None
    else:
        max_bid = max_bid_dict['amount__max']
    return (max_bid)


def get_minimum_bid(ad):
    """Returns the minimum value a user can bid on an ad"""
    current_max_bid = get_max_bid(ad)
    if current_max_bid is None:
        min_bid = ad.reserve
    else:
        min_bid = current_max_bid + 100
    return min_bid

def update_user_rating(user):
    all_ads = Advertisement.objects.filter(seller=user)
    total = 0
    count = 0
    for ad in all_ads:
        if ad.rating:
            total += ad.rating
            count += 1
    try:
        average = total / count
    except ZeroDivisionError:
        average = 0
    profile = user.userprofile
    profile.rating = average
    profile.save()
