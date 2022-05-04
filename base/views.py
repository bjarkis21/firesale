from django.shortcuts import render

# Create your views here.
from ads.models import Category

adv = [
    {'id':1, 'title':'First ad', 'price':'$100'},
    {'id':2, 'title':'Second ad', 'price':'$200'},
    {'id':3, 'title':'Third ad', 'price':'$300'},
]

def home(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'home.html', context)

def ads(request):
    context = {'adv':adv}
    return render(request, 'ads.html', context)
