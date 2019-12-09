from django.core.management.base import BaseCommand, CommandError
import datetime
import csv
import os
from st.models import st_model

class Command(BaseCommand):
    help = 'Export the Squirrel data to csv file'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str)

    def handle(self, *args, **options):
        model = st_model
        meta = model._meta
        fields = [f.name for f in meta.fields]

        with open(options['path'], 'w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(fields)
            for obj in model.objects.all():
                writer.writerow([getattr(obj, att) for att in fields])
