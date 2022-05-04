from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from user import views

urlpatterns = [
    path('register', views.register, name='Nýskrá'),
    path('login', LoginView.as_view(template_name='user/login.html'), name='Innskrá'),
    path('logout', LogoutView.as_view(next_page='login'), name='Útskrá'),
    path('profile', views.profile, name='profile'),
    path('bankinfo', views.bank_info, name='bank-info')
]