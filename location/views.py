import re
from django.shortcuts import render
from django.http import JsonResponse
from .models import School
import requests


# Create your views here.
def Index(request):
    school = School.objects.all()
    return render(request, 'index.html', {"school": school})

def get_url(request):
    short_url = request.POST.get("short_url")
    try:
        res = requests.head(short_url, allow_redirects=False)
        if res.status_code in range(300, 310):
            long_url = res.headers['Location']
            g_coord = get_coordinates(long_url)
        return JsonResponse(g_coord)
    except requests.ConnectionError as e:
        return 


def get_coordinates(url: str) -> dict:
    match = re.search(r'@(-?\d+\.\d+),(-?\d+\.\d+)', url)
    if match:
        return {
            "latitude": float(match.group(1)),
            "longitude": float(match.group(2))
        }
    return {"erro":"no coordinates"}