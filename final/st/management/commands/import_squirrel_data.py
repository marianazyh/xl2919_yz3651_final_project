import csv
from st.models import st_model
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Import the Squirrel Data'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str)

    def handle(self,*args, **options): 
        with open(options['path']) as sd:
            data = csv.DictReaderi(sd)
            next(data)
            for row in data:
                
                sm = st_model()
                
                sm.latitude_coordinate=row['X']
                sm.longitude_coordinate=row['Y']
                sm.unique_squirrel_id=row['Unique Squirrel ID']
                sm.shift=row['Shift']
                sm.date=row['Date']
                sm.age=row['Age']
                sm.primary_fur_color=row['Primary Fur Color']
                sm.location=row['Location']
                sm.specific_location=row['Specific Location']
                sm.running=row['Running']
                sm.chasing=row['Chasing']
                sm.climbing=row['Climbing']
                sm.eating=row['Eating']
                sm.foraging=row['Foraging']
                sm.other_activities=row['Other Activities']
                sm.kuks=row['Kuks']
                sm.quaas=row['Quaas']
                sm.moans=row['Moans']
                sm.tail_flags=row['Tail flags']
                sm.tail_twitches=row['Tail twitches']
                sm.approaches=row['Approaches']
                sm.indifferent=row['Indifferent']
                sm.runs_from=['Runs from']
                
                sm.save()


