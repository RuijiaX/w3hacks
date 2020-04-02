# Generated by Django 2.2.9 on 2020-04-02 06:55

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=300)),
                ('prize', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Hackathon',
            fields=[
                ('id', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=300)),
                ('start_datetime', models.DateTimeField()),
                ('end_datetime', models.DateTimeField()),
                ('awards', models.ManyToManyField(blank=True, to='main.Award')),
            ],
        ),
        migrations.CreateModel(
            name='PastHackathon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=300)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('awards', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, max_length=20, null=True)),
                ('biography', models.TextField(blank=True, max_length=200, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('education', models.CharField(blank=True, max_length=100, null=True)),
                ('location', models.CharField(blank=True, max_length=50, null=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='')),
                ('skills', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), blank=True, null=True, size=None)),
                ('joined_date', models.DateField()),
                ('past_hackathons', models.ManyToManyField(blank=True, to='main.Hackathon')),
                ('past_non_w3hacks_hackathons', models.ManyToManyField(blank=True, to='main.PastHackathon')),
            ],
        ),
        migrations.CreateModel(
            name='ResourceLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('url_extension', models.CharField(max_length=50)),
                ('link', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ScheduleEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=300)),
                ('event_link', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SocialLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social_network', models.CharField(max_length=50)),
                ('link', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=500)),
                ('project_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('technologies_used', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=30), blank=True, null=True, size=None)),
                ('github_link', models.CharField(blank=True, max_length=200, null=True)),
                ('video_link', models.CharField(blank=True, max_length=200, null=True)),
                ('extra_files', django.contrib.postgres.fields.ArrayField(base_field=models.FileField(upload_to=''), blank=True, null=True, size=None)),
                ('likes', models.IntegerField(blank=True, null=True)),
                ('comments', models.ManyToManyField(blank=True, to='main.Comment')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='projects',
            field=models.ManyToManyField(blank=True, to='main.Project'),
        ),
        migrations.AddField(
            model_name='profile',
            name='social_links',
            field=models.ManyToManyField(blank=True, to='main.SocialLink'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='hackathon',
            name='competitors',
            field=models.ManyToManyField(blank=True, to='main.Profile'),
        ),
        migrations.AddField(
            model_name='hackathon',
            name='resources',
            field=models.ManyToManyField(blank=True, to='main.ResourceLink'),
        ),
        migrations.AddField(
            model_name='hackathon',
            name='schedule',
            field=models.ManyToManyField(blank=True, to='main.ScheduleEvent'),
        ),
        migrations.AddField(
            model_name='hackathon',
            name='submissions',
            field=models.ManyToManyField(blank=True, to='main.Project'),
        ),
        migrations.AddField(
            model_name='hackathon',
            name='themes',
            field=models.ManyToManyField(blank=True, to='main.Theme'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.Profile'),
        ),
    ]
