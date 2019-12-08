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
    return render(request,'st/sightings.html',context)

def showstats(request):
    squirrel = st_model.objects.all()
    count_am = squirrel.values('shift').annotate(am_count = Count('shift')).filter(shift='AM')
    count_pm = squirrel.values('shift').annotate(am_count = Count('shift')).filter(shift='PM')
    count_adult = squirrel.values('age').annotate(adult_count = Count('age')).filter(age='Adult')
    count_juvenile = squirrel.values('age').annotate(juvenile_count = Count('age')).filter(age='Juvenile')
    count_above = squirrel.values('location').annotate(above_count = Count('location')).filter(location='Above Ground')
    count_plane = squirrel.values('location').annotate(plane_count = Count('location')).filter(location='Ground Plane')
    count_running = squirrel.values('running').annotate(count_running=Count('running')).filter(running="True")
    count_eating = squirrel.values('eating').annotate(count_eating=Count('eating')).filter(eating="True")
    context = {
        'count_am':count_am,
        'count_pm':count_pm,
        'count_adult':count_adult,
        'count_juvenile':count_juvenile,
        'count_above':count_above,
        'above_plane':count_plane,
        'count_running':count_running,
        'count_eating':count_eating,
        }
    return render(request,'st/stats.html',context)

def add(request):
    return True

def edit(request, unique_squirrel_id):
    return True
