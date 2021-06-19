from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    ''' create a profile object when new
    user created with user instance '''
    if created:
        Profile.objects.create(user=instance)
