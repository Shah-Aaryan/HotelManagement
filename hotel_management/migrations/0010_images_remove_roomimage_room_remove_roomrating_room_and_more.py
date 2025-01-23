# Generated by Django 4.2.4 on 2023-11-22 17:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hotel_management', '0009_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image_url', models.ImageField(upload_to='pics')),
            ],
        ),
        migrations.RemoveField(
            model_name='roomimage',
            name='room',
        ),
        migrations.RemoveField(
            model_name='roomrating',
            name='room',
        ),
        migrations.RemoveField(
            model_name='userreview',
            name='room',
        ),
        migrations.RemoveField(
            model_name='room',
            name='image_url',
        ),
        migrations.AddField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='rating',
            field=models.FloatField(default='5'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='AdditionalImage',
        ),
        migrations.DeleteModel(
            name='RoomImage',
        ),
        migrations.DeleteModel(
            name='RoomRating',
        ),
        migrations.DeleteModel(
            name='UserReview',
        ),
        migrations.AddField(
            model_name='room',
            name='images',
            field=models.ManyToManyField(to='hotel_management.images'),
        ),
    ]
