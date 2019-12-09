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
    return render(request,'st/front.html',context)


def showstats(request):
    squirrel = st_model.objects.all()
    count_shift = squirrel.values('shift').order_by('shift').annotate(shift_count = Count('shift'))
    count_adult = count_adult=st_model.objects.filter(age='Adult').count()
    count_juvenile = st_model.objects.filter(age='Juvenile').count()
    count_above = st_model.objects.filter(location='Above Ground').count()
    count_plane = st_model.objects.filter(location='Ground Plane').count()
    count_running = squirrel.values('running').annotate(count_running=Count('running')).filter(running="True")
    count_eating = squirrel.values('eating').annotate(count_eating=Count('eating')).filter(eating="True")
    context = {
        'count_shift':count_shift,
        'count_adult':count_adult,
        'count_juvenile': count_juvenile,
        'count_above':count_above,
        'count_plane': count_plane,
        'count_running':count_running,
        'count_eating':count_eating,
        }
    return render(request,'st/stats.html',context)


def add(request):
    if request.method == 'POST':
        form = st_form(request.POST)
        if form.is_valid():
            new = form.save()
            print('New sighting is valid and added to our dataset!')
        else:
            print('Sighting information inputed is invalid and cannot be added! Please try again!')
    else:
        form = st_form()
    
    context = {
            'form': form,
            }
    return render(request, 'st/add.html', context)
    

def edit(request, unique_squirrel_id):
    orginial = st_model.objects.get(unique_squirrel_id = unique_squirrel_id)
    if request.method == 'POST':
        form = st_form(request.POST, instance = original)
        if form.is_valid():
            form.save()
            print(f'Updated Information of squirrel {unique_squirrel_id} has been saved!')
        else:
            print(f'Sighting information inputed is invalid and cannot be updated! Please try again!')
    else:
        form = st_form(instance = original)

    context = {
            'form': form,
            }
    return render(request, 'st/edit.html',context)


