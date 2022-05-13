from django.shortcuts import render

# Create your views here.

adv = [
    {'id':1, 'title':'First ad', 'price':'$100'},
    {'id':2, 'title':'Second ad', 'price':'$200'},
    {'id':3, 'title':'Third ad', 'price':'$300'},
    {'id':4, 'title':'Fourth ad', 'price':'$4000'},
]

def home(request):
    context = {'adv': adv}
    return render(request, 'home.html')

def ads(request):
    context = {'adv':adv}
    return render(request, 'ads.html', context)
