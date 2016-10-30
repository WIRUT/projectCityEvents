from django.db.models.signals import  post_save
from django.dispatch import receiver
from .models import CustomEvent


@receiver(post_save, sender=CustomEvent)
def updatephotolocation(sender, instance, created, **kwargs):
	if not instance._disable_signals:
		print "im in the post save"
		instance.save_without_signals()






