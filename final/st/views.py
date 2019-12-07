from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse
from .models import st_model
from .forms import st_form



def showmap(request):
    sightings = st_model.objects.all()
    context = {
        'sightings': sightings,
    }
    return render(request, 'st/map.html', context)

def sightings(request):
    return True

def showstats(request):
    return True

def add(request):
    return True

def edit(request, unique_squirrel_id):
    return True
