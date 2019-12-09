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
                sm. created = st_model.objects.get_or_create(
                                latitude_coordinate=row['Y'],
                                longitude_coordinate=row['X'],
                                unique_squirrel_id=row['Unique Squirrel ID'],
                                shift=row['Shift'],
                                date=row['Date'],
                                age=row['Age'],
                                primary_fur_color=row['Primary Fur Color'],
                                location=row['Location'],
                                specific_location=row['Specific Location'],
                                running=verify(row['Running']),
                                chasing=verify(row['Chasing']),
                                climbing=verify(row['Climbing']),
                                eating=verify(row['Eating']),
                                foraging=verify(row['Foraging']),
                                other_activities=row['Other Activities'],
                                kuks=verify(row['Kuks']),
                                quaas=verify(row['Quaas']),
                                moans=verify(row['Moans']),
                                tail_flags=verify(row['Tail flags']),
                                tail_twitches=verify(row['Tail twitches']),
                                approaches=verify(row['Approaches']),
                                indifferent=verify(row['Indifferent']),
                                runs_from=verify(row['Runs from']),
                                )
                if created:
                    sm.save()



