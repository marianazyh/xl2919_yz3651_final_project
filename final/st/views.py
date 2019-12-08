from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import st_model
from .forms import st_form
from django.db.models import Count
from django.contrib import messages


def showmap(request):
    sightings = st_model.objects.all()
    context = {
            'sightings': sightings
    }
    return render(request, 'st/map.html', context)

def sightings(request):
    squirrels = st_model.objects.all()
    context = {
            'squirrels':squirrles
    }
    return render(request,'st/sightings',context)

def showstats(request):
    count_squirrles = st_models.objects.value('Unique Squirrel ID').annotate(s_count = Count('Unique Squirrel ID'))
    count_am = st_models.objects.value('Shift').annotate(am_count = Count('AM'))
    count_pm = st_models.objects.value('Shift').annotate(am_count = Count('PM'))
    count_adult = st_models.objects.value('Age').annotate(adult_count = Count('Adult'))
    count_juvenile = st_models.objects.value('Age').annotate(juvenile_count = Count('Juvenile'))
    count_above = st_models.objects.value('Location').annotate(above_count = Count('Above Ground'))
    count_plane = st_models.objects.value('Location').annotate(plane_count = Count('Ground Plane'))
    count_running = st_models.objects.filter(running=True).Count()
    count_eating = st_models.objects.filter(eating= True).Count()
    context = {
        'count_squirrles':count_squirrles,
        'count_am':count_am,
        'count_pm':count_pm,
        'count_adult':count_adult,
        'count_juvenile':count_juvenile,
        'count_above':count_above,
        'above_plane':count_plane,
        'count_running':count_running,
        'count_eating':count_eating,
        }
    return render(request,'st/sightings/stats',context)

def add(request):
    return True

def edit(request, unique_squirrel_id):
    return True
