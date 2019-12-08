from django.shortcuts import render
from st.models import st_model
import random

# Create your views here.
def showmap(request):
    selection = random.sample(range(st_model.objects.count()),100)
    sightings =[st_model.objects.all()[i] for i in selection]
    context = {
            'sightings': sightings,
    }
    return render(request, 'st/map.html', context)
