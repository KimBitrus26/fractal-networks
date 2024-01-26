from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import GeoPoint

def index(request):

    if request.method == 'POST':
        
        name = request.POST['name']
        latitude = float(request.POST['latitude'])
        longitude = float(request.POST['longitude'])

        print("lat", latitude)
        print("long", longitude)

        GeoPoint.objects.create(name=name, location=(longitude, latitude))

        messages.success(request, f"Test Geopoint created successfully.")
        return HttpResponseRedirect(reverse('home'))

    return render(request, 'index.html')