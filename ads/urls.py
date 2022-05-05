from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.ads, name='ads'),
    path('create_ad1', views.create_ad1, name='create-ad1'),
    path('create_ad2', views.create_ad2, name='create-ad2')
]