from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=30)
    location = models.TextField()
    description = models.TextField()

    registration_open = models.BooleanField(default=False)
    event_date = models.DateTimeField()

    def __str__(self):
        return self.name

    def GetAllAttendees(self):
        return Registration.objects.filter(related_event=self)

    def GetAllConfirmedAttendees(self):
        return self.GetAllAttendees().filter(paid=True)

    def GetAllPendingAttendees(self):
        return self.GetAllAttendees().filter(paid=False)

class Registration(models.Model):
    related_event = models.ForeignKey(Event)
    related_user = models.ForeignKey(User)

    date_created = models.DateTimeField(auto_now_add=True, name="date_registered", verbose_name="Date Registered")

    paid = models.BooleanField(default=False)
    date_paid = models.DateTimeField(null=True)

class Access(models.Model):
    related_registration = models.ForeignKey(Registration)

    date_created = models.DateTimeField(auto_now_add=True, name="date_entered", verbose_name="Date Entered")

class Payment(models.Model):
    related_registration = models.ForeignKey(Registration)

    date_created = models.DateTimeField(auto_now_add=True, name="data_paid", verbose_name="Date Paid")


