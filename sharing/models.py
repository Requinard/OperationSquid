from django.db import models
from django.contrib.auth.models import User
from events.models import Event
from django.db.models.signals import pre_delete
from django.dispatch import receiver

# Create your models here.
class Message(models.Model):
    related_user = models.ForeignKey(User)
    related_event = models.ForeignKey(Event)
    related_message = models.ForeignKey('Message', null=True, blank=True)
    related_categories = models.ManyToManyField('Category')

    title = models.CharField(max_length=20)
    body = models.TextField(null=True)
    file= models.FileField(upload_to='documents/%Y/%m/%d/%H/%M/%S', null=True, blank=True)


    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_created',)

    def __len__(self):
        return len(Comment.objects.filter(related_message=self))


class Comment(models.Model):
    related_message = models.ForeignKey(Message)
    related_user = models.ForeignKey(User)

    body = models.TextField()

    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body

    class Meta:
        ordering = ("-date_created",)

class Appointment(models.Model):
    related_event = models.ForeignKey(Event)

    date = models.DateField()

    start_time = models.TimeField()
    end_time = models.TimeField()

    title = models.CharField(max_length=20)
    body = models.TextField()

    class Meta:
        ordering = ("date", "start_time")

class News(models.Model):
    related_event = models.ForeignKey(Event)

    date_posted = models.DateTimeField(auto_now_add=True)

    title = models.CharField(max_length=24)
    body = models.TextField()

    class Meta:
        ordering = ("-date_posted", )

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


@receiver(pre_delete, sender=Message)
def DeleteRelatedMedia(sender, instance=None, **kwargs):
    if instance is not None:
        instance.file.delete()