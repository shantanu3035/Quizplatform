from django.db.models.signals import post_save
from users.models import CustomUser
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=CustomUser)
def createProfile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(email=instance)

@receiver(post_save, sender=CustomUser)
def saveProfile(sender, instance, **kwargs):
    instance.profile.save()