from projectCityEvents.eventful import Eventful
from projectCityEvents.eventfulCallWrite import eventfulCallWrite
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from projectCityEvents.searchManager import searchManager
from itertools import chain
from operator import attrgetter
import requests
import json

def results(request, search_key, page):
	
	manager = searchManager()
	events = manager.getEventfulEvents(search_key, page)
	userEvents = manager.getUserEvents(search_key, page)
	
	events = sorted(
		chain(events, userEvents),
		key=attrgetter('start_time'))

	if int(page) > 1 and len(events) < 8*int(page):
		message="no further results could be found"
		return render(request, 'dashboard/event_list.html', {'events':events, 'search_key':search_key, 'page':page, 'message':message })
	
	return render(request, 'dashboard/event_list.html', {'events':events, 'search_key':search_key, 'page':page })

def showMore(request, search, pageNo):
	eventfulAPIKeys = Eventful()
	pageNo = int(pageNo)+1
	search_list = ""
	
	try:
		if "+" in search:
			search_list 		= search.split("+")
		
		if search_list == "":
			response 			= requests.get(eventfulAPIKeys.getSearchURL() + search + eventfulAPIKeys.getPage() + str(pageNo))
		
		elif len(search_list)==2:
			response 			= requests.get(eventfulAPIKeys.getSearchURL() + search_list[0] + eventfulAPIKeys.getPage() + str(pageNo) + eventfulAPIKeys.getCity() + search_list[1])
		
		elif len(search_list)==3:
			response 			= requests.get(eventfulAPIKeys.getSearchURL() + search_list[0] + eventfulAPIKeys.getPage() + str(pageNo) + eventfulAPIKeys.getDate() + str(search_list[1]).replace("-", "") + "-" + str(search_list[2]).replace("-", ""))
		
		else:
			response 			= requests.get(eventfulAPIKeys.getSearchURL() + search_list[0] + eventfulAPIKeys.getPage() + str(pageNo) + eventfulAPIKeys.getCity() + eventfulAPIKeys.getDate() + str(search_list[2]).replace("-", "") + "-" + str(search_list[3]).replace("-", ""))
		apiToDatabase = eventfulCallWrite()
		apiToDatabase.storeEventDetails(response.json())
		return HttpResponseRedirect(reverse('dashboard:results', kwargs={'search_key':search, 'page': pageNo}))
	except:
		return HttpResponseRedirect(reverse('dashboard:results', kwargs={'search_key':search, 'page': pageNo}))
