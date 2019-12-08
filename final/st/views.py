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
    count_shift = squirrel.values('shift').order_by('shift').annotate(shift_count = Count('shift'))
    count_age = squirrel.values('age').order_by('age').annotate(adult_count = Count('age'))
    count_location = squirrel.values('location').order_by('location').annotate(above_count = Count('location'))
    count_running = squirrel.values('running').annotate(count_running=Count('running')).filter(running="True")
    count_eating = squirrel.values('eating')..annotate(count_eating=Count('eating')).filter(eating="True")
    context = {i
        'count_shift':count_shift,
        'count_age':count_age,
        'counte_location':count_location,
        'count_running':count_running,
        'count_eating':count_eating,
        }
    return render(request,'st/stats.html',context)

def add(request):
    return True

def edit(request, unique_squirrel_id):
    return True
