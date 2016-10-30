from userCreateEvents.models import *
from eventSearch.models import *
import datetime

class searchManager():

	def getEventfulEvents(self, search_key, page_number):
		number_of_results 		= int(page_number)*8
		search_list = ""

		if "+" in search_key:
			search_list 		= search_key.split("+")
		
		if search_list=="":
			events 				= Event.objects.filter(searchtags__contains=search_key)[:(number_of_results)]
		
		elif len(search_list)==2:
			events 				= Event.objects.filter(searchtags__contains=search_list[0]).filter(searchtags__contains=search_list[1])[:(number_of_results)]
		
		elif len(search_list)==3:
			events 				= Event.objects.filter(searchtags__contains=search_list[0]).filter(start_time__gte=search_list[1]).filter(start_time__lte=search_list[2])[:(number_of_results)]
		
		else:
			events 				= Event.objects.filter(searchtags__contains=search_list[0]).filter(searchtags__contains=search_list[1]).filter(start_time__gte=search_list[2]).filter(start_time__lte=search_list[3])[:(number_of_results)]
		
		for event in events:
			if event.venue:
				event.venue.name 		= event.venue.name.encode("UTF-8")
				if event.venue.address is not None:
					event.venue.address 	= event.venue.address.encode("UTF-8")
		return events

	def getUserEvents(self, search_key, page_number):
		number_of_results 		= int(page_number)*2
		search_list = ""
		
		if "+" in search_key:
			search_list 		= search_key.split("+")
		
		if search_list=="":
			userEvents 			= CustomEvent.objects.filter(searchtags__contains=search_key).filter(isAuthenticated=True)[:(number_of_results)]
		
		elif len(search_list)==2:
			userEvents 			= CustomEvent.objects.filter(searchtags__contains=search_list[0]).filter(searchtags__contains=search_list[1]).filter(isAuthenticated=True)[:(number_of_results)]
		
		elif len(search_list)==3:
			userEvents 			= CustomEvent.objects.filter(searchtags__contains=search_list[0]).filter(start_time__gte=search_list[1]).filter(start_time__lte=search_list[2]).filter(isAuthenticated=True)[:(number_of_results)]
		
		else:
			userEvents 			= CustomEvent.objects.filter(searchtags__contains=search_list[0]).filter(searchtags__contains=search_list[1]).filter(start_time__gte=search_list[2]).filter(start_time__lte=search_list[3]).filter(isAuthenticated=True)[:(number_of_results)]
		return userEvents
