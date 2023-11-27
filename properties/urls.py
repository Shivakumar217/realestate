# urls.py

from django.urls import path
from .views import property_listing, save_property,saved_properties,update_description, remove_property

urlpatterns = [
    path('property-listing/', property_listing, name='property-listing'),
    path('save-property/', save_property, name='save-property'),
    path('saved-properties/', saved_properties, name='saved-properties'),
    path('update-description/<int:property_id>/', update_description, name='update_description'), 
    path('remove-property/<int:property_id>/', remove_property, name='remove_property'), 
  
    
    
    # Other patterns if any...
]
