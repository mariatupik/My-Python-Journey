from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'profile-form-input'}),
            'email': forms.EmailInput(attrs={'class': 'profile-form-input'}),
        }

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['img', 'gender', 'is_delivery']
        widgets = {
            'gender': forms.Select(attrs={'class': 'profile-form-input'}),
            'is_delivery': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }