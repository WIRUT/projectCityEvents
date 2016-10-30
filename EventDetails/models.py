from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils import timezone
from decimal import Decimal

from eventSearch.models import Event
from accounts.models import UserProfile
from userCreateEvents.models import CustomEvent
from django.contrib.auth.models import User

class RSVPList(models.Model):
	event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
	user = models.TextField(default='', blank=True)
	def __str__(self):
		return self.event_id	
		
class VoteList(models.Model):
	event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
	user = models.TextField(default='', blank=True)
	def __str__(self):
		return self.event_id

class RSVPCustomList(models.Model):
	title = models.ForeignKey(CustomEvent, on_delete=models.CASCADE)
	user = models.TextField(default='', blank=True)
	def __str__(self):
		return self.title

class VoteCustomList(models.Model):
	title = models.ForeignKey(CustomEvent, on_delete=models.CASCADE)
	user = models.TextField(default='', blank=True)
	def __str__(self):
		return self.title