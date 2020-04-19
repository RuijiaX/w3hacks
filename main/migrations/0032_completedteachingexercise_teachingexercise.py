# Generated by Django 3.0.4 on 2020-04-19 01:19

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_completedvisualizationexercise_visualizationexercise'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeachingExercise',
            fields=[
                ('id', models.CharField(default=main.models.generate_id, max_length=8, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('prerequisites', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), blank=True, null=True, size=None)),
                ('difficulty_level', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.DifficultyLevel')),
                ('resources', models.ManyToManyField(blank=True, to='main.ResourceLink')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.Topic')),
            ],
        ),
        migrations.CreateModel(
            name='CompletedTeachingExercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formats', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), size=None)),
                ('teaching_exercise_link', models.CharField(max_length=200)),
                ('score', models.IntegerField(blank=True, null=True)),
                ('teaching_exercise', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.TeachingExercise')),
            ],
        ),
    ]
