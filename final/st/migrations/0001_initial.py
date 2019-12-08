# Generated by Django 3.0 on 2019-12-08 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='st_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude_coordinate', models.FloatField(max_length=20)),
                ('longitude_coordinate', models.FloatField(max_length=20)),
                ('unique_squirrel_id', models.CharField(help_text='ID Format: Hectare-Shift-MMDD-Hectare Squirrel Number', max_length=30)),
                ('shift', models.CharField(choices=[('AM', 'AM'), ('PM', 'PM')], max_length=2)),
                ('date', models.DateField(help_text='MMDDYYYY')),
                ('age', models.CharField(blank=True, choices=[('Adult', 'Adult'), ('Juvenile', 'Juvenile')], max_length=10)),
                ('primary_fur_color', models.CharField(blank=True, choices=[('Gray', 'Gray'), ('Cinnamon', 'Cinnamon'), ('Black', 'Black'), ('White', 'White')], max_length=100)),
                ('location', models.CharField(blank=True, choices=[('Above Ground', 'Above Ground'), ('Ground Plane', 'Ground Plane')], max_length=100)),
                ('specific_location', models.CharField(blank=True, help_text='Anything about the sighting location you would like to specify in 200 characters or less.', max_length=200)),
                ('running', models.BooleanField()),
                ('chasing', models.BooleanField()),
                ('climbing', models.BooleanField()),
                ('eating', models.BooleanField()),
                ('foraging', models.BooleanField()),
                ('other_activities', models.CharField(blank=True, help_text="Anything about the squirrel's activities you would like to specify in 200 characters or less.", max_length=200)),
                ('kuks', models.BooleanField()),
                ('quaas', models.BooleanField()),
                ('moans', models.BooleanField()),
                ('tail_flags', models.BooleanField()),
                ('tail_twitches', models.BooleanField()),
                ('approaches', models.BooleanField()),
                ('indifferent', models.BooleanField()),
                ('runs_from', models.BooleanField()),
            ],
        ),
    ]
