from django.db import models

# Create your models here.
class BaseReservation(models.Model):
    resource = models.CharField(max_length=30)
    class Meta:
        abstract = True

class Spot(BaseReservation):
    name = models.CharField(max_length=30)

class Item(BaseReservation):
    resource_id = models.CharField(max_length=30)