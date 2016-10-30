from projectCityEvents.eventful import Eventful
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from projectCityEvents.eventfulCallWrite import eventfulCallWrite
from projectCityEvents.searchManager import searchManager
from django.utils.html import strip_tags
from django.shortcuts import render
from .forms import EventSearchForm
from ipware.ip import get_real_ip
import geoip2.database
import datetime
import requests 


def getUserIP(request):
	ip = get_real_ip(request)
	if ip is not None:
		print ip
		return ip
	else:
		print "Unable to detect ip address."
		return 0 

def getCityByIP(request):
	geoDB = 'static/geodata/GeoLite2-City.mmdb'
	reader = geoip2.database.Reader(geoDB)
	ip = getUserIP(request)
	if ip > 0:
		response = reader.city(ip)
		return response.city.name
	else:
		return "Vancouver"

def getCountryByIP(request):
	geoDB = 'static/geodata/GeoLite2-City.mmdb'
	reader = geoip2.database.Reader(geoDB)
	ip = getUserIP(request)
	if ip > 0:
		response = reader.country(ip)
		return response.country.iso_code
	else:
		return "CA"

def getTodayDate():
	now = datetime.datetime.now()
	month = str(now.month).zfill(2)
	date = str(now.day).zfill(2)
	year = str(now.year)
	return month + '/' + date + '/' + year

def Eventful_Search(request):
	city = getCityByIP(request)
	country = getCountryByIP(request)
	date = getTodayDate()
	if request.method=="POST":
		form 					 = EventSearchForm(request.POST)
		eventfulAPIKeys			 = Eventful()
		additionalParameters	 = ""
	
		if form.is_valid():
			search_key 			 	= strip_tags(form.cleaned_data['search_keyword'])
	
			if "+" in search_key:
				search_key 				= search_key.replace("+", " ")
			search_list 		 	= search_key
	
			if form.cleaned_data['search_city']:
				search_city 			= strip_tags(form.cleaned_data['search_city'])
				if "," in search_city:
					temp = search_city.split(",")
					search_city = temp[0]
				search_city 			+= "," + form.cleaned_data['search_country']
				print search_city
				
				if "+" in search_city:
					search_city 			= search_city.replace("+", " ")
				additionalParameters 	+= eventfulAPIKeys.getCity() + search_city
				search_list 			+= "+" + search_city
	
			if form.cleaned_data['search_from_date']:
				from_date 				= form.cleaned_data['search_from_date']
				to_date 				= from_date + datetime.timedelta(days=365)
				from_date_eventful 		= str(from_date).replace("-", "")
				to_date_eventful 		= str(to_date).replace("-", "")
				search_list 			+= "+" + str(from_date) + "+" + str(to_date)
				additionalParameters 	+= eventfulAPIKeys.getDate() + str(from_date_eventful) + "-" + str(to_date_eventful)
	
			page = 1
	
			print "api call start"

			if additionalParameters!="":
				response 				= requests.get(eventfulAPIKeys.getSearchURL() + search_key + eventfulAPIKeys.getPage() + str(page) + additionalParameters)
				print "api call end"
			else:
				response 				= requests.get(eventfulAPIKeys.getSearchURL() + search_key + eventfulAPIKeys.getPage() + str(page))
				print "api call end"
			apiToDatabase 			= eventfulCallWrite()
	
			try:
				apiToDatabase.storeEventDetails(response.json())
				manager = searchManager()
				userEvents = manager.getUserEvents(search_list, page)
				events = manager.getEventfulEvents(search_list, page)

				if len(userEvents)>0 or len(events)>0:
					return HttpResponseRedirect(reverse('dashboard:results', kwargs={'search_key':search_list, 'page':page}))
				else:
					form = EventSearchForm()
					message = "Your search returned no results, try a more general search"
					return render(request, 'eventSearch/event_search.html', {'form':form, 'message':message})
	
			except TypeError:
				manager = searchManager()
				userEvents = manager.getUserEvents(search_list, page)
				events = manager.getEventfulEvents(search_list, page)

				if len(userEvents)>0 or len(events)>0:
					return HttpResponseRedirect(reverse('dashboard:results', kwargs={'search_key':search_list, 'page':page}))
				else:
					form = EventSearchForm()
					message = "Your search returned no results, try a more general search"
					return render(request, 'eventSearch/event_search.html', {'form':form, 'message':message})

			except:	
				print "eventful reject"
				manager = searchManager()
				userEvents = manager.getUserEvents(search_list, page)
				events = manager.getEventfulEvents(search_list, page)
				if len(userEvents)>0 or len(events)>0:
					return HttpResponseRedirect(reverse('dashboard:results', kwargs={'search_key':search_list, 'page':page}))
				else:
					message = "Your search returned no results, try a more general search"
					return render(request, 'eventSearch/event_search.html', {'form':form, 'message':message})
	
	else: 
		form = EventSearchForm(initial={'search_city':city, 'search_from_date': date, 'search_country': country})
	return render(request, 'eventSearch/event_search.html', {'form':form})
