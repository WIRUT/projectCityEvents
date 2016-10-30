from __future__ import unicode_literals

from django.db import models
from eventSearch.models import *
from django.contrib.auth.models import User

class savedEvents(models.Model):
	event = models.ForeignKey(Event, on_delete=models.CASCADE)
	user = models.TextField(default='', blank=True)