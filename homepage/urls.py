# homepage/urls.py
from django.urls import path , include
from .views import homepage, about, contact_us

urlpatterns = [
    path('', homepage, name='homepage'),
    path('about/', about, name='about'),
    path('contact-us/', contact_us, name='contact-us'),
    path('properties/', include('properties.urls')),
]
