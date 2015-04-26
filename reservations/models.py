from django.db import models
from events.models import Event
# Create your models here.
class BaseReservation(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=6)
    relatedEvent = models.ForeignKey(Event)
    class Meta:
        abstract = True

class Spot(BaseReservation):
    isNoisy = models.BooleanField()
    isFarAway = models.BooleanField()
    isCloseToBathroom = models.BooleanField()
    isTent = models.BooleanField()

    capacity = models.SmallIntegerField()

class Item(BaseReservation):
    amountAvailable = models.SmallIntegerField()
    image = models.FileField(upload_to='equipment/%Y/%m/%d/%H/%M/%S', null=True, blank=True)