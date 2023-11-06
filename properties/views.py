import json
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, ListView
import requests
from .models import Property

class PropertyCreateView(CreateView):
    model = Property
    template_name = 'properties/property_form.html'
    fields = ['title', 'description', 'price', 'is_sold', 'rating']
    success_url = '/properties/'

class PropertyListView(ListView):
    model = Property
    template_name = 'properties/property_list.html'
    context_object_name = 'properties'
    


def rate_property(request, property_id):
    property = get_object_or_404(Property, pk=property_id)
    if request.method == 'POST':
        rating = request.POST.get('rating')
        property.rating = rating
        property.save()
    return redirect('property-list')
    
