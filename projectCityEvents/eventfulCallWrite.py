from django.core.exceptions import ObjectDoesNotExist
from projectCityEvents.eventful import Eventful
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from eventSearch.models import * 
import requests 
import json
from django.db import transaction

def printJSON(payload):
	print json.dumps(
			payload, sort_keys=True,
			indent=4, separators=(',', ': '))

@transaction.atomic()
def setEventDetails(event_details):
	
	try:

		event = Event.objects.get(eventID=event_details['id'])
		return None
	
	except ObjectDoesNotExist:
	
		event = Event(
			title 			= event_details['title'],
			eventID 		= event_details['id'],
			description 	= event_details['description'],
			url 			= event_details['url'],
			owner 			= event_details['owner'],
			region_abbr 	= event_details['region_abbr'],
			region_name 	= event_details['region_name'],
			city_name 		= event_details['city_name'],
			postal_code 	= event_details['postal_code'],
			country_name 	= event_details['country_name'],
			country_abbr 	= event_details['country_abbr'],
			latitude 		= event_details['latitude'],
			longitude 		= event_details['longitude'],
			geocode_type 	= event_details['geocode_type'],
			start_time 		= event_details['start_time'],
			stop_time 		= event_details['stop_time'],
			created_time 	= event_details['created'],
			last_modified 	= event_details['modified'],
			price 			= event_details['price']
			)
		event.save()
		return event

@transaction.atomic()
def setEventVenue(event_details, eventKey):

	try:

		newVenue = Venue.objects.get(venueID=event_details['venue_id'])

	except ObjectDoesNotExist:

		newVenue = Venue(
			address = event_details['venue_address'],
			venueID = event_details['venue_id'],
			name = event_details['venue_name'],
			url = event_details['venue_url'],
			latitude = event_details['latitude'],
			longitude = event_details['longitude'],
		)
		newVenue.save()

	eventKey = Event.objects.get(eventID=event_details['id'])
	eventKey.venue = newVenue
	eventKey.save()

@transaction.atomic()
def setEventImages(event_details, eventKey):
	event_image = event_details['image']
	
	if event_image is not None: 
	
		if eventKey.image_set.all().count()<1 or not eventKey.image_set.all():
	
			image = Image(
				width_med 	= int(event_image['medium']['width']),
				height_med 	= int(event_image['medium']['height']),
				url_med 	= event_image['medium']['url'],
				width_lg 	= int(event_image['large']['width']),
				height_lg	= int(event_image['large']['height']),
				url_lg	 	= event_image['large']['url'],
				event 		= eventKey,	
				)
			image.save()
	
	else:
	
		print 'No image to save.'


def setEventPerformers(event_details, eventKey):
	
	performers = event_details['performers']
	
	if performers is not None:
	
		if len(performers['performer'])!=6:
	
			performer_list = performers['performer']
	
			for artist in performer_list:

				with transaction.atomic():
	
					try:
						performer = Performer.objects.get(performerID=artist['id'])

					except ObjectDoesNotExist:
						performer = Performer(
							name = artist['name'],
							url = artist['url'], 
							bio = artist['short_bio'],
							performerID = artist['id'],
						)
						performer.save()
					eventKey.performers.add(performer)
	
		else:
	
			with transaction.atomic():

				try:
					performer = Performer.objects.get(performerID=performers['performer']['id'])

				except ObjectDoesNotExist:
					performer = Performer(
						name = performers['performer']['name'],
						url = performers['performer']['url'], 
						bio = performers['performer']['short_bio'],
						performerID = performers['performer']['id'],
					)
					performer.save()
				eventKey.performers.add(performer)
	
	else:
	
		print 'No performers listed.'

class eventfulCallWrite():
	def storeEventDetails(self, event_list):
		
		if event_list is None:
		
			print "No events returned."
		
		else:
		
			events = event_list['events']['event']
			a = 0

			if event_list['total_items'] != "1":
		
				for i in events:
					a += 1
					print 'Event: ' + str(a)
					event = setEventDetails(i)
			
					if event is not None:
						setEventImages(i, event)
						setEventPerformers(i, event)
						setEventVenue(i, event)

						with transaction.atomic():
							event = Event.objects.get(eventID=event.eventID)
							if event.title:
								search_tags = event.title + " "
							if event.venue:
								search_tags += event.venue.name + " "
							if event.city_name:
								search_tags += event.city_name + "," + event.country_abbr + " "
							for performer in event.performers.all():
								search_tags += performer.name
							event.searchtags = search_tags
							event.save()

			else:

					event = setEventDetails(events)
			
					if event is not None:
						setEventImages(i, events)
						setEventPerformers(i, events)
						setEventVenue(i, events)

						with transaction.atomic():
							event = Event.objects.get(eventID=event.eventID)
							if event.title:
								search_tags = event.title + " "
							if event.venue:
								search_tags += event.venue.name + " "
							if event.city_name:
								search_tags += event.city_name + "," + event.country_abbr + " "
							for performer in event.performers.all():
								search_tags += performer.name
							event.searchtags = search_tags
							event.save()
			print str(len(events)) + " events successfully transferred to the database."
