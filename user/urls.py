from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from user import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),
    path('profile', views.profile, name='profile'),
    path('bankinfo', views.bank_info, name='bank-info')
]