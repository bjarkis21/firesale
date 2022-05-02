from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('advertisements/', views.advertisements, name='advertisements'),
]