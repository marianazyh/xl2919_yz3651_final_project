# Generated by Django 3.0 on 2019-12-08 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('st', '0003_auto_20191208_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='st_model',
            name='age',
            field=models.CharField(blank=True, choices=[('Adult', 'Adult'), ('Juvenile', 'Juvenile'), ('Unknown_age', 'Unknown_age')], max_length=30),
        ),
    ]
