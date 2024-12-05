import json
from django.contrib import messages
import re
from django.shortcuts import redirect, render
from django.http import JsonResponse
from .models import School
import requests
from geopy.distance import geodesic


# Create your views here.
def Index(request):
    return render(request, 'index.html', {"school": School.objects.all()})

def addPlace(request):
    """
    For adding a new school"""
    if request.method == 'POST':
        place = request.POST.get('place')
        google_map = request.POST.get('mapURL')
        school = School.objects.create(sch_name=place, google_map=google_map)
        school.save()
        messages.success(request,"Success")
        return redirect('index')
    messages.success(request,"Invalid mehod")
    return redirect('index')
async def get_full_url(schoolID: int) -> str:
    school = await School.objects.aget(id=schoolID)
    location_short_url = str(school.google_map)
    res = requests.head(location_short_url, allow_redirects=False)
    if res.status_code in range(300, 310):
        return res.headers['Location']
    

async def getDistance(request, sch_id):
    if request.method == 'POST':
        google_map = await get_full_url(int(sch_id))
        school_cordinates = await get_coordinates(google_map)
        body = json.loads(request.body)
        user_coordinates = (body['userLongitude'], body['userLatitude'])

        distance = geodesic(school_cordinates, user_coordinates).km
        return JsonResponse({"distance": f"{distance:.2f}"})
    return JsonResponse({"error":"Invalid method"})

async def get_coordinates(url: str) -> tuple:
    match = re.search(r'@(-?\d+\.\d+),(-?\d+\.\d+)', url)
    if match:
        return (float(match.group(1)), float(match.group(2)))