# Generated by Django 4.0.8 on 2024-08-25 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transport',
            name='engine_type',
            field=models.CharField(max_length=255),
        ),
    ]
