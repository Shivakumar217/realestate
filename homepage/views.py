# In your views.py file
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm



def homepage(request):
    return render(request, 'homepage/homepage.html')

def about(request):
    return render(request, 'homepage/about.html')

def contact_us(request):
    return render(request, 'homepage/contact_us.html')




# views.py
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            request.session['user_authenticated'] = True
            # Redirect to the homepage or any other desired page
            return redirect('homepage')
        else:
            messages.error(request, 'Invalid login credentials.')

    # Clear the session flag to avoid showing success message on subsequent requests
    if 'user_authenticated' in request.session:
        del request.session['user_authenticated']

    return render(request, 'homepage/login.html')

def user_logout(request):
    logout(request)
    messages.success(request, 'Logout successful.')
    return redirect('homepage')  # Redirect to the homepage or any other desired page
