# Generated by Django 4.0.8 on 2024-08-26 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_alter_transport_car_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='transport',
            name='engine_power',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
