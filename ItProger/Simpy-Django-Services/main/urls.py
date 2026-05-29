from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('uslugi/', views.uslugi, name='uslugi'),
    path('contact/', views.contact, name='contact'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.login_view, name='login'),
]
