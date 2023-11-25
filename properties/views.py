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
