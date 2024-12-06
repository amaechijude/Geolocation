import json
from django.contrib import messages
import re
from django.shortcuts import redirect, render
from django.http import JsonResponse
from .models import Location
import requests
from geopy.distance import geodesic

# Create your views here.
# Home view
def Index(request):
    return render(request, 'index.html', {"location": Location.objects.all()})


# Add a new location
def addPlace(request):
    """
    For adding a new Location
    :param request: The request object
    :return: A redirection to the home page or an error message
    """
    if request.method == 'POST':
        place = request.POST.get('place')
        google_map = request.POST.get('mapURL')
        new_location = Location.objects.create(sch_name=place, google_map=google_map)
        new_location.save()
        messages.success(request,"Success")
        return redirect('index')
    messages.success(request,"Invalid mehod")
    return redirect('index')

# Get the distance from the user's location to the place's location
async def getDistance(request, location_id):
    """
    Get the distance from the user's location to the place's location
    :param request: The request object
    :param sch_id: The ID of the location
    :return: A JSON response containing the distance in kilometers
    """
    if request.method == 'POST':
        google_map = await get_full_url(int(location_id))
        school_cordinates = await get_coordinates(google_map)
        body = json.loads(request.body)
        user_coordinates = (body['userLongitude'], body['userLatitude'])

        distance = geodesic(school_cordinates, user_coordinates).km
        return JsonResponse({"distance": f"{distance:.2f}"})
    return JsonResponse({"error":"Invalid method"})


# Get full url path for short google map url
async def get_full_url(location_id: int) -> str:
    """
    Get the full URL for the given short Google map URL
    :param location_id: The ID of the location
    :Return a full url path for google map
    """
    current_location = await Location.objects.aget(id=location_id)
    location_short_url = str(current_location.google_map)
    res = requests.head(location_short_url, allow_redirects=False)
    if res.status_code in range(300, 310):
        return res.headers['Location']
    

# Get the coordinates from the Google map URL
async def get_coordinates(url: str) -> tuple:
    """
    Get the coordinates from the Google map URL
    :param url: The Google map URL
    :return: The coordinates as a tuple (longitude, latitude)
    """
    match = re.search(r'@(-?\d+\.\d+),(-?\d+\.\d+)', url)
    if match:
        return (float(match.group(1)), float(match.group(2)))