from django.db.models import Max

from ads.models import BidsOn


def get_max_bid(ad):
    """Return maximum current bid on a single ad"""
    max_bid_dict = BidsOn.objects.filter(advertisement=ad).aggregate(Max('amount'))
    if max_bid_dict is None:
        max_bid = None
    else:
        max_bid = max_bid_dict['amount__max']
    return max_bid


def get_minimum_bid(ad):
    """Returns the minimum value a user can bid on an ad"""
    current_max_bid = get_max_bid(ad)
    if current_max_bid is None:
        min_bid = ad.reserve
    else:
        min_bid = current_max_bid + 1
    return min_bid
