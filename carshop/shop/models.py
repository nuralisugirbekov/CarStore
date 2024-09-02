from django.db import models
from django.utils import timezone

# Car / Lorry
class Category(models.Model):
    title = models.CharField(max_length=255)
    created_at=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Transport(models.Model):
    title = models.CharField(max_length=255)
    car_picture = models.CharField(max_length=255)
    price = models.FloatField()
    engine_type = models.CharField(max_length=255)
    engine_power = models.IntegerField()
    engine_volume = models.FloatField()
    rating = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
