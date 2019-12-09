from django.shortcuts import render
from st.models import st_model
import random

# A view that shows a map that displays the location of the squirrel sightings
def showmap(request):

    # randomly select 100 sightings from the imported data to avoid freezing
    selection = random.sample(range(st_model.objects.count()),100)

    # create sightings list
    sightings =[st_model.objects.all()[i] for i in selection]
    
    # context to display
    context = {
            'sightings': sightings,
    }
    return render(request, 'st/map.html', context)
