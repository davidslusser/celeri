from django.db.models.signals import post_save
from django.dispatch import receiver
from djangoaddicts.signalcontrol.decorators import signal_control

# import models
from casemgr.models import Booking


@receiver(post_save, sender=Booking)
def new_booking(sender, instance, created, **kwargs):
    """ """
    if created:
        print(f"Got a new booking {instance.booking_id}; send message to clerk office")
