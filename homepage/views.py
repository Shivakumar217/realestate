# homepage/views.py
from django.shortcuts import render

def homepage(request):
    return render(request, 'homepage/homepage.html')

def about(request):
    return render(request, 'homepage/about.html')

def contact_us(request):
    return render(request, 'homepage/contact_us.html')

def properties(request):
    return render(request, 'properties/property_list.html')
