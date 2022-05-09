from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from ads.models import Category
from user import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', LoginView.as_view(template_name='user/login.html', extra_context={'categories': Category.objects.all()}), name='login'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),
    path('profile', views.profile, name='profile'),
    path('bankinfo', views.bank_info, name='bank-info'),
    path('myproducts', views.myproducts, name='myproducts'),
    path('mybids', views.mybids, name='mybids'),
    path('salehistory', views.salehistory, name='salehistory'),
    path('purchases', views.purchases, name='purchases')

]