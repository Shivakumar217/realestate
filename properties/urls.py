# properties/urls.py
from django.urls import path
from .views import ( 
    PropertyCreateView,
    PropertyListView,
    rate_property,
   
)

urlpatterns = [   
    path('property/add/', PropertyCreateView.as_view(), name='property-create'),
    path('property/rate/<int:property_id>/', rate_property, name='rate-property'),
    path('', PropertyListView.as_view(), name='property-list'),
   
]
