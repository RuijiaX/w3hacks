# Generated by Django 2.2.9 on 2020-07-04 06:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20200703_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 3, 23, 11, 5, 174013)),
        ),
        migrations.AlterField(
            model_name='event',
            name='type',
            field=models.CharField(choices=[('Hackathon', 'Hackathon'), ('Codeathon', 'Codeathon'), ('Challenge', 'Challenge'), ('Workshop', 'Workshop'), ('Showcase', 'Showcase')], max_length=50),
        ),
    ]
