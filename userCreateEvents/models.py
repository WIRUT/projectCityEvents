from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
import os


## TODO: Look into hosting a picture for the event
## Possibly a unique event ID
## need to change starttime & stop time to include hours
## search tags and performers should be like 'Tags'

# returns the path for eventphoto at /media/eventphotos/username/eventtitle/file.jpg

def get_image_path(instance, filename):
    return os.path.join('eventphotos', str(instance.owner), str(instance.title), filename)


class CustomEvent(models.Model):
	title			 = models.CharField(max_length=200, blank=False)
	performers		 = models.CharField(max_length=200, blank=False)
	description 	 = models.TextField(blank=False)
	searchtags		 = models.TextField(blank=True)
	venue_name		 = models.CharField(max_length=200, blank=False)
	votes			 = models.PositiveIntegerField(default=0)
	# owner should connect to the current logged-in user
	owner			 = models.ForeignKey(User, null=True)
	country_name	 = CountryField(blank_label='(select country)' )
	city_name	 	 = models.CharField(max_length=60, blank=False )
	region_name		 = models.CharField(max_length=60, blank=False )
	address		     = models.CharField(max_length=200, blank=False)
	latitude	 	 = models.DecimalField(decimal_places=9, max_digits=20, blank=True,null=True)
	longitude		 = models.DecimalField(decimal_places=9, max_digits=20, blank=True, null=True)
	price 			 = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null =True)
	ticket_URL 	     = models.URLField(max_length=200,blank=True,null=True)
	start_time	 	 = models.DateTimeField()
	stop_time		 = models.DateTimeField(blank=False)
	created_time	 = models.DateTimeField()
	last_modified	 = models.DateTimeField(blank=False) 
	eventphoto		 = models.ImageField(upload_to=get_image_path, blank=True,null=True)
	isAuthenticated  = models.BooleanField(default=False)
	spotifyURL		 = models.CharField(max_length=200, null=True)

	def __init__(self, *args, **kwargs):
		super(CustomEvent, self).__init__(*args, **kwargs)
		self._disable_signals = False

	def save_without_signals(self):
		"""
		This allows for updating the model from code running inside post_save()
		signals without going into an infinite loop:
		"""
		self._disable_signals = True
		self.save()
		self._disable_signals = False
	
	def __str__(self):
		return self.title

