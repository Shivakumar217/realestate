# properties/urls.py
from django.urls import path
from .views import (
<<<<<<< HEAD
    
    PropertyCreateView,
    rate_property,
    
)

urlpatterns = [
    
=======
    PropertyCreateView,
    rate_property,
   )

urlpatterns = [
>>>>>>> fe8bbefd688c366333bc171f991201c5c97085b3
    path('property/add/', PropertyCreateView.as_view(), name='property-create'),
    path('property/rate/<int:property_id>/', rate_property, name='rate-property'),
   
]
