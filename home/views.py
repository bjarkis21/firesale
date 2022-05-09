from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


# Create your views here.
from ads.models import Category

adv = [
    {'id':1, 'title':'First ad', 'price':'$100'},
    {'id':2, 'title':'Second ad', 'price':'$200'},
    {'id':3, 'title':'Third ad', 'price':'$300'},
]


def home(request):
    return redirect('ads')