from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_delete

# Create your models here.
class UserPrivilege(models.Model):
    related_user = models.OneToOneField(User, related_name="privilege")

    level = models.IntegerField(choices=(
        (1, "User"),
        (2, "Employee"),
        (3, "Editor"),
        (4, "Administrator")
    ), default=1)

    @receiver(post_save, sender=User)
    def CreateUserPrivilege(sender, instance=None, created=False, **kwargs):
        if created:
            privilege = UserPrivilege(related_user=instance)
            privilege.save()

    @receiver(pre_delete, sender=User)
    def DeleteUserPrivilege(sender, instance=None, **kwargs):
        if instance is not None:
            privilege = UserPrivilege.objects.get(related_user=User)
            privilege.delete()


class UserProfile(models.Model):
    related_user = models.OneToOneField(User, related_name="profile")

    @receiver(post_save, sender=User)
    def CreateUserProfile(sender, instance=None, created=False, **kwargs):
        if created:
            p = UserProfile(related_user=instance)
            p.save()

    @receiver(pre_delete, sender=User)
    def DeleteUserProfile(sender, instance=None, **kwargs):
        if instance:
            p = UserProfile.objects.get(related_user=instance)
            p.delete()


class UserSettings(models.Model):
    related_user = models.OneToOneField(User, related_name="settings")

    @receiver(post_save, sender=User)
    def CreateUserSettings(sender, instance=None, created=False, **kwargs):
        if created:
            p = UserSettings(related_user=instance)
            p.save()

    @receiver(pre_delete, sender=User)
    def DeleteUserSettings(sender, instance=None, **kwargs):
        if instance:
            p = UserSettings.objects.get(related_user=instance)
            p.delete()