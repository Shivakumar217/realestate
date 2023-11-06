import json
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView
from .models import Property

class PropertyListView(ListView):
    model = Property
    template_name = 'properties/property_list.html'
    context_object_name = 'properties'

class PropertyCreateView(CreateView):
    model = Property
    template_name = 'properties/property_form.html'
    fields = ['title', 'description', 'price', 'is_sold', 'rating']
    success_url = '/properties/'