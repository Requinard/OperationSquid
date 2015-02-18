from django.db import models
from django.contrib.auth.models import User
from events.models import Event
# Create your models here.
class Message(models.Model):
    related_user = models.ForeignKey(User)
    related_event = models.ForeignKey(Event)
    related_message = models.ForeignKey('Message', null=True, blank=True)
    related_categories = models.ManyToManyField('Category')

    title = models.CharField(max_length=20)
    body = models.TextField(null=True)
    file = models.FileField(upload_to='documents/%Y/%m/%d/%H/%M/%S', null=True, blank=True)

    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_created',)

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name