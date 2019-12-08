from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import st_model
from .forms import st_form
from django.db.models import Count
from django.contrib import messages



def sightings(request):
    squirrels = st_model.objects.all()
    context = {
            'squirrels':squirrels
    }
    return render(request,'st/sightings',context)

def showstats(request):
    squirrel = st_model.objects.all()
    count_squirrles = squirrel.values('Unique Squirrel ID').annotate(s_count = Count('Unique Squirrel ID'))
    count_am = squirrel.values('Shift').annotate(am_count = Count('AM'))
    count_pm = squirrel.values('Shift').annotate(am_count = Count('PM'))
    count_adult = squirrel.values('Age').annotate(adult_count = Count('Adult'))
    count_juvenile = squirrel.values('Age').annotate(juvenile_count = Count('Juvenile'))
    count_above = squirrel.values('Location').annotate(above_count = Count('Above Ground'))
    count_plane = squirrel.values('Location').annotate(plane_count = Count('Ground Plane'))
    count_running = squirrel.values('Running').annotate(count_running=Count('Running')).filter(Running="True")
    count_eating = squirrel.values('Running').annotate(count_eating=Count('Eating')).filter(Eating="True")
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
