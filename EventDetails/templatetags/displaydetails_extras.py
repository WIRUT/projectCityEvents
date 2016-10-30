from django import template
from eventSearch.models import Event

from userCreateEvents.models import CustomEvent
from itertools import chain

register = template.Library()

#@register.inclusion_tag('EventDetails/displaydetails.html')
@register.simple_tag
def getRecentEvents():
	"""Returns most 3 most recent events & 1 custom event"""
	recents = Event.objects.all().order_by('-created_time')[:2]
	#recents = Event.objects.order_by(-'created_time')[:5]
	#return {'recents': recents}
	
	#SHOULD WORK IN THEORY
	recents = list(chain(CustomEvent.objects.all().order_by('-created_time')[:1], recents)) #for adding custom events to the list of recommended events
	
	return recents