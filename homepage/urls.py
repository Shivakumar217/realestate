# homepage/urls.py
from django.urls import path

from properties.views import property_listing , save_property , saved_properties , update_description , remove_property
from .views import homepage, about, contact_us, user_login

urlpatterns = [
    path('', homepage, name='homepage'),
    path('about/', about, name='about'),
    path('contact-us/', contact_us, name='contact-us'),
    path('login/', user_login, name='user_login'),
    path('property-listing/', property_listing, name='property_listing'),
    path('save-property/', save_property, name='save-property'),
    path('saved-properties/', saved_properties, name='saved-properties'),
    # Other patterns if any...
    

]
   