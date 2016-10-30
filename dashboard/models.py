from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Location(models.Model):
    message_text = models.CharField(max_length=200) 
    longitude = models.FloatField(default=0)
    latitude = models.FloatField(default=0)

    def getLongitude(self):
        return self.longitude

    def getLatitude(self):
        return self.latitude

    def __str__(self):
        return self.message_text

class EventSearchModel(models.Model):
	event_ID			 = models.CharField(max_length=200)
	event_Name 		 	 = models.CharField(max_length=200)
	event_Category    	 = models.CharField(max_length=200)
	event_City		 	 = models.CharField(max_length=200)
	event_VenueName		 = models.CharField(max_length=200)
	event_venueID		 = models.CharField(max_length=200)
	event_Date 	 	 	 = models.DateField()
	event_Description 	 = models.TextField()
	event_Longitutde	 = models.DecimalField(decimal_places=15, max_digits=20)
	event_Latitude	 	 = models.DecimalField(decimal_places=15, max_digits=20)
	event_Owner			 = models.CharField(max_length=200)
	event_Is_User_Going	 = models.BooleanField() 

	def __str__(self):
		return self.eventName

	def getEventVenueName(self):
		return self.eventLocation

	def getEventCategory(self):
		return self.eventCategory

	def getEventDate(self):
		return self.eventDate

	def getEventDescription(self):
		return self.eventDescription

	def getEventLongitude(self):
		return self.eventLongitutde

	def getEventLatitude(self):
		return self.eventLatitude

	def getEventOwner(self):
		return self.eventOwner

	def isUserGoing(self):
		return self.eventIsUserGoing