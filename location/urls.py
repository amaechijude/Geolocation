from django.urls import path
from . import views
urlpatterns = [
    path('', views.Index, name='index'),
    path('get_url/<int:id>', views.get_url, name='get_url')
]