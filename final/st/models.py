from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class st_model(models.Model):

    latitude_coordinate = models.FloatField(
            max_length=20,
            )
    
    longitude_coordinate = models.FloatField(
            max_length=20,
            )

    unique_squirrel_id = models.CharField(
            max_length=30,
            help_text=('ID Format: Hectare-Shift-MMDD-Hectare Squirrel Number'),
            )


    AM = 'AM'
    PM = 'PM'

    shift_choices = (
        (AM,'AM'),
        (PM,'PM'),
        )

    shift = models.CharField(
        max_length=2,
        choices=shift_choices,
        )   

    date = models.DateField(
        help_text=_('MMDDYYYY'),
        )

    Adult = 'Adult'
    Juvenile = 'Juvenile'

    age_choices = (
            (Adult, 'Adult'),
            (Juvenile, 'Juvenile'),
            )

    age = models.CharField(
            max_length=10,
            choices=age_choices,
            blank=True,
            )
    
    Gray = 'Gray'
    Cinnamon = 'Cinnamon'
    Black = 'Black'
    White = 'White'

    p_color_choices = (
            (Gray, 'Gray'),
            (Cinnamon, 'Cinnamon'),
            (Black, 'Black'),
            (White, 'White'),
            )

    primary_fur_color = models.CharField(
            max_length=100,
            choices=p_color_choices,
            blank=True,
            ) 
    
    AG = 'Above Ground'
    GP = 'Ground Plane'

    location_choices = (
            (AG, 'Above Ground'),
            (GP, 'Ground Plane'),
            )

    location = models.CharField(
            max_length=100,
            choices=location_choices,
            blank=True,
            ) 

    specific_location = models. CharField(
            max_length=200,
            help_text=('Anything about the sighting location you would like to specify in 200 characters or less.'),
            blank=True,
            )

    running = models.BooleanField()

    chasing = models.BooleanField()

    climbing = models.BooleanField() 

    eating = models.BooleanField()

    foraging = models.BooleanField()

    other_activities = models.CharField(
            max_length=200,
            help_text=("Anything about the squirrel's activities you would like to specify in 200 characters or less."),
            blank=True,
            )

    kuks = models.BooleanField()

    quaas = models.BooleanField()

    moans = models.BooleanField()

    tail_flags = models.BooleanField()

    tail_twitches = models.BooleanField()

    approaches = models.BooleanField()

    indifferent = models.BooleanField()

    runs_from = models.BooleanField()

