from django.http import JsonResponse
from django.shortcuts import render
import requests

def property_listing(request):
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        # This is an AJAX request
        zipcode = request.GET.get('zipcode', '03102')  # Default to ZIP code 03102 if not provided
        url = "https://zillow-com1.p.rapidapi.com/propertyExtendedSearch"
        querystring = {"location": zipcode, "home_type": "Houses"}
        headers = {
            "X-RapidAPI-Key": "9c8a477140mshc82f717cfb57878p15504ajsn053b9994aef4",
            "X-RapidAPI-Host": "zillow-com1.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
        api_data = response.json()
        
        if isinstance(api_data, list):
            properties = []  # or some other appropriate handling for a list
        else:
            properties = api_data.get("props", [])

     
        return JsonResponse({'properties': properties})
    
    return render(request, 'properties/listing_ajax.html')

# views.py
from django.shortcuts import render
from django.http import JsonResponse
from .models import Property

def save_property(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        zpid = request.POST.get('zpid')

        # Check if the property already exists in the database
        existing_property = Property.objects.filter(zpid=zpid).first()

        if existing_property:
            return JsonResponse({'status': 'error', 'message': 'Property already saved.'}, status=400)

        # Create a new Property instance and save it to the database
        new_property = Property(address=address, zpid=zpid)
        new_property.save()
        

        return JsonResponse({'status': 'success', 'message': 'Property saved successfully.'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=400)

