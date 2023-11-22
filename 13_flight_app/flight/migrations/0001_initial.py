# Generated by Django 4.2.7 on 2023-11-17 17:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_number', models.CharField(max_length=4, unique=True)),
                ('operating_airlines', models.CharField(max_length=50)),
                ('departure_city', models.CharField(max_length=85)),
                ('arrival_city', models.CharField(max_length=85)),
                ('date_of_departure', models.DateField()),
                ('estimated_time_of_departure', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=1019)),
                ('last_name', models.CharField(max_length=666)),
                ('email', models.EmailField(max_length=345)),
                ('phone_number', models.PositiveBigIntegerField()),
                ('update_date', models.DateField(auto_now=True)),
                ('created_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flights', to='flight.flight')),
                ('passenger', models.ManyToManyField(to='flight.passenger')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]