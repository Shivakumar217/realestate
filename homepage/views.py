# In your views.py file
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm



def homepage(request):
    return render(request, 'homepage/homepage.html')

def about(request):
    return render(request, 'homepage/about.html')

def contact_us(request):
    return render(request, 'homepage/contact_us.html')




# homepage/views.py

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('homepage')  # Redirect to the homepage or any other desired page
        else:
            messages.error(request, 'Invalid login credentials.')

    return render(request, 'homepage/login.html')

