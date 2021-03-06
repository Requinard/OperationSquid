from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.timezone import datetime

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

    def GetOpenTag(self):
        if self.event_date.date() == datetime.now().date():
            return "success"
        elif self.event_date.date() > datetime.now().date():
            return "primary"
        else:
            return "warning"

    class Meta:
        ordering = ["-event_date"]


class Registration(models.Model):
    related_event = models.ForeignKey(Event)
    related_user = models.ForeignKey(User)

    date_created = models.DateTimeField(auto_now_add=True, name="date_registered", verbose_name="Date Registered")

    paid = models.BooleanField(default=False)
    date_paid = models.DateTimeField(null=True)

    def __str__(self):
        return "%s registered for %s" % (self.related_user.get_full_name(), self.related_event.name)


class Access(models.Model):
    related_registration = models.ForeignKey(Registration)

    date_created = models.DateTimeField(auto_now_add=True, name="date_entered", verbose_name="Date Entered")


class Payment(models.Model):
    related_registration = models.ForeignKey(Registration)

    date_created = models.DateTimeField(auto_now_add=True, name="data_paid", verbose_name="Date Paid")

    def __str__(self):
        return self.related_registration.related_event.name


@receiver(pre_save, sender=Payment)
def SetRegistrationAsSaved(sender, instance=None, **kwargs):
    if instance is not None:
        instance.related_registration.paid = True
        instance.related_registration.save()

