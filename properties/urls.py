# urls.py

from django.urls import path
from .views import property_listing, save_property

urlpatterns = [
    path('property-listing/', property_listing, name='property-listing'),
   
    
    
    # Other patterns if any...
]
