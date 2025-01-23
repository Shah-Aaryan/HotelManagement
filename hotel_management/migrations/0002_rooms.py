# Generated by Django 4.2.4 on 2023-11-01 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image_url', models.ImageField(upload_to='pics')),
                ('rooms', models.IntegerField()),
                ('bathrooms', models.IntegerField()),
                ('balcony', models.IntegerField()),
                ('sofa', models.IntegerField()),
                ('room_heater', models.BooleanField()),
                ('ac', models.BooleanField()),
                ('wifi', models.BooleanField()),
                ('tv', models.BooleanField()),
                ('adults', models.IntegerField()),
                ('children', models.IntegerField()),
                ('location', models.CharField(max_length=255)),
                ('price_per_night', models.FloatField()),
            ],
        ),
    ]
