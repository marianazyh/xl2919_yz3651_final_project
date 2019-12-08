import csv
from st.models import st_model
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Import the Squirrel Data'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str)

    def handle(self,*args, **options): 

        def verify(key):
            if key.lower() == 'true':
                return True
            elif key.lower() == 'false':
                return False
            else:
                return 'N/A'


        with open(options['path']) as sd:
            data = csv.DictReader(sd)
            next(data)
            st_model.objects.all().delete()
            for row in data:
                
                sm = st_model()
                
                sm.latitude_coordinate=row['Y']
                sm.longitude_coordinate=row['X']
                sm.unique_squirrel_id=row['Unique Squirrel ID']
                sm.shift=row['Shift']
                sm.date=row['Date']
                sm.age=row['Age']
                sm.primary_fur_color=row['Primary Fur Color']
                sm.location=row['Location']
                sm.specific_location=row['Specific Location']
                sm.running=verify(row['Running'])
                sm.chasing=verify(row['Chasing'])
                sm.climbing=verify(row['Climbing'])
                sm.eating=verify(row['Eating'])
                sm.foraging=verify(row['Foraging'])
                sm.other_activities=row['Other Activities']
                sm.kuks=verify(row['Kuks'])
                sm.quaas=verify(row['Quaas'])
                sm.moans=verify(row['Moans'])
                sm.tail_flags=verify(row['Tail flags'])
                sm.tail_twitches=verify(row['Tail twitches'])
                sm.approaches=verify(row['Approaches'])
                sm.indifferent=verify(row['Indifferent'])
                sm.runs_from=verify(row['Runs from'])
                
                sm.save()


