from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('uslugi/', views.uslugi, name='uslugi'),
    path('profile/', views.profile, name='profile'),
]
