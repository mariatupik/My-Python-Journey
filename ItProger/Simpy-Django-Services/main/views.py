from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm  
from .forms import ProfileUpdateForm, UserUpdateForm, ContactForm
from .models import Profile
from django.contrib import messages
from django.core.mail import send_mail

def index(request):
    return render(request, 'main/index.html')

def uslugi(request):
    return render(request, 'main/uslugi.html')

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Дані успішно змінено!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'main/profile.html', {
        'u_form': u_form,
        'p_form': p_form
    })
def login_view(request):
    if request.user.is_authenticated:
        return redirect('profile')  

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"З поверненням, {username}!")
                
                next_url = request.GET.get('next')
                if next_url:
                    return redirect(next_url)
                return redirect('profile')
        else:
            messages.error(request, "Неправильний username або password.")
    else:
        form = AuthenticationForm()
        
    return render(request, 'main/login.html', {'form': form})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_instance = form.save()
        
            subject = contact_instance.subject
            plain_message = contact_instance.message
            from_email = f"From <{contact_instance.email}>"
            to_email = "your_receiver_email@gmail.com" 
            
            try:
                send_mail(subject, plain_message, from_email, [to_email])
            except Exception:
                pass
            messages.success(request, 'Повідомлення успішно надіслано!')
            return redirect('contact')
    else:
        form = ContactForm()
        
    return render(request, 'main/contact.html', {'form': form})