import csv
from st.models import st_model
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Import the Squirrel Data'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str)

    def handle(self,*args, **options): 
        # create a function to verify the boolean input
        def verify(key):
            if key.lower() == 'true':
                return True
            elif key.lower() == 'false':
                return False
            else:
                return 'N/A'

        # open the csv given a path in string form
        with open(options['path']) as sd:
            data = csv.reader(sd,delimiter=',')
            next(data,None)
       
            # delete existing dataset before importing a new dataset
            st_model.objects.all().delete()
       
            for row in data:

                # make sure squirrel ids are indeed unique
                if st_model.objects.filter(unique_squirrel_id=row[2]).exists():
                    continue
                
                # import data
                sm, created = st_model.objects.get_or_create(
                                latitude_coordinate=row[1],
                                longitude_coordinate=row[0],
                                unique_squirrel_id=row[2],
                                shift=row[4],
                                date=row[5],
                                age=row[7],
                                primary_fur_color=row[8],
                                location=row[12],
                                specific_location=row[14],
                                running=verify(row[15]),
                                chasing=verify(row[16]),
                                climbing=verify(row[17]),
                                eating=verify(row[18]),
                                foraging=verify(row[19]),
                                other_activities=row[20],
                                kuks=verify(row[21]),
                                quaas=verify(row[22]),
                                moans=verify(row[23]),
                                tail_flags=verify(row[24]),
                                tail_twitches=verify(row[25]),
                                approaches=verify(row[26]),
                                indifferent=verify(row[27]),
                                runs_from=verify(row[28]),
                                )
                if created:
                    sm.save()



