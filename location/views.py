import re
from django.shortcuts import render
from django.http import JsonResponse
from .models import School
import requests
from geopy.distance import geodesic


# Create your views here.
def Index(request):
    school = School.objects.all()
    return render(request, 'index.html', {"school": school})

def get_url(request, id):
    sch = School.objects.get(id=id)
    short_url = str(sch.google_map)
    res = requests.head(short_url, allow_redirects=False)
    if res.status_code in range(300, 310):
        long_url = res.headers['Location']
        print(long_url)
        g_coord = get_coordinates(long_url)
    return JsonResponse(g_coord)


def get_coordinates(url: str) -> dict:
    match = re.search(r'@(-?\d+\.\d+),(-?\d+\.\d+)', url)
    if match:
        x =  {
            "latitude": float(match.group(1)),
            "longitude": float(match.group(2))
        }
        print(x)
        return x
    return {"erro":"no coordinates"}