from django.urls import path
from . import views
urlpatterns = [
    path('', views.Index, name='index'),
    path('getDistance/<int:location_id>', views.getDistance, name='getDistance'),
    path('addPlace', views.addPlace, name='addPlace'),
]