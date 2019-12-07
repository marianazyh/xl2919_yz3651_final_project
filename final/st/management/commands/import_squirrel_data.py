import csv
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help= 'Import the Squirrel Data'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str)

    def handle(self,*args, **options): 
        with open(options['path']) as sd:
            data = csv.DictReader(sd)


