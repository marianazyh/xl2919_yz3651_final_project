from django.urls import path

from . import views

urlpatterns = [
    path('map/', views.showmap, name='showmap'),
    path('sightings', views.sightings, name='sightings'),
    path('sightings/stats', views.showstats, name='showstats'),
    path('sightings/add', views.add, name='add'),
    path('sightings/<unique_squirrel_id>', views.edit, name='edit'),
]
