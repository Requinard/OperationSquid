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


class Comment(models.Model):
    related_message = models.ForeignKey(Message)
    related_user = models.ForeignKey(User)

    body = models.TextField()

    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body

    class Meta:
        ordering = ("-date_created",)

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


@receiver(pre_delete, sender=Message)
def DeleteRelatedMedia(sender, instance=None, **kwargs):
    if instance is not None:
        instance.file.delete()