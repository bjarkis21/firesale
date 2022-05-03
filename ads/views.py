from django.shortcuts import render

# Create your views here.
adv = [
    {'id':1, 'title':'First ad', 'price':'$100'},
    {'id':2, 'title':'Second ad', 'price':'$200'},
    {'id':3, 'title':'Third ad', 'price':'$300'},
]

def advertisements(request):
    context = {'adv':adv}
    return render(request, 'ads.html', context)

def create_ad(request):
    pass