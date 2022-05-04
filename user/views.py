from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from ads.models import Category
from user.forms.profile_forms import ProfileForm, BankInfoForm
from user.models import UserProfile

# Create your views here.



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'user/register.html', {
        'form': UserCreationForm(),
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
    if request.method == 'POST':
        form = BankInfoForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save()
            return redirect(redirect_url)
    return render(request, 'user/bank_info.html', {
        'form': BankInfoForm(instance=profile),
        'categories': Category.objects.all()
    })