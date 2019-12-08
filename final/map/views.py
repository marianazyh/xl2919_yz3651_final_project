from django.shortcuts import render
from .models import st_model


# Create your views here.
def showmap(request):
    sightings = st_model.objects.all()
    context = {
            'sightings': sightings
    }
    return render(request, 'st/map.html', context)
