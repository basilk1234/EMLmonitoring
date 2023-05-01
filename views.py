# views.py

from django.shortcuts import render
from .models import EmergencyLight

def index(request):
    # this method receives the HTTP request, stores all EML objects inside emergency_lights
    emergency_lights = EmergencyLight.objects.all()
    # returns and renders request, html template with all EML objects. 
    return render(request, 'index.html', {'emergency_lights': emergency_lights})
