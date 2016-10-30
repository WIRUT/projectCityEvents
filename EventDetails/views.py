from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.core.urlresolvers import reverse
from django.views import generic
from django.core.exceptions import ObjectDoesNotExist
from eventSearch.models import Event
from saveEvents.models import *
from django.db.models import Q
from django.db import transaction
from userCreateEvents.models import CustomEvent
from .models import RSVPList, VoteList, RSVPCustomList, VoteCustomList
import spotipy


# function to get artist id given the performer from event_dtails. BUGGED, somehow the if statement doesnt work
def getArtistID(artist):
	spotify = spotipy.Spotify()	
	print "artist is %s" %str(artist)
	result = spotify.search(q=str(artist), type='artist')
	try:
		link = str(result['artists']['items'][0]['external_urls']['spotify'])
		spotifyartistID = link.split('/')[-1]
		return "https://embed.spotify.com/?uri=spotify:artist:" + spotifyartistID
	except:
	# if there was an issue getting the artists ID, just return empty string back
		print "exception caused"
		return ""

# snippet from setEventDetails function to get the embeededspotifyURL into event


def EventDetailsView(request,pk):

	event = get_object_or_404(Event,pk=pk)
	try:
		# get first performer and print it on the details page
		performer =event.performers.all()
		embeddedspotifyURL = getArtistID(performer[0])

	except:
	#	if there is no performer listed  from the spotify call, return an empty string
		embeddedspotifyURL =""
		print "exception caused"

	event.spotifyURL = embeddedspotifyURL
	event.save() 

	return render(request,'eventdetails/displaydetails.html', {'event':event})

def CustomEventDetailsView(request,pk):

	event = get_object_or_404(CustomEvent,pk=pk)
	try:
		# get first performer and print it on the details page
		performer =event.performers.all()
		embeddedspotifyURL = getArtistID(performer[0])

	except:
	#	if there is no performer listed  from the spotify call, return an empty string
		embeddedspotifyURL =""
		print "exception caused"

	event.spotifyURL = embeddedspotifyURL
	event.save() 

	return render(request,'eventdetails/displaycustomdetails.html', {'event':event})

@login_required
@transaction.atomic
def saveEvent(request, pk):
	theevent = get_object_or_404(Event, pk=pk)
	try:
		test = savedEvents.objects.get(Q(event=pk) & Q(user=request.user.get_username()))
	except (KeyError, savedEvents.DoesNotExist):
		theevent.savedevents_set.create(user=request.user.get_username())
		return HttpResponseRedirect(reverse('EventDetails:eventdetails', args=(pk,)))
	else:
		#https://docs.djangoproject.com/en/1.9/ref/contrib/messages/
		messages.error(request, 'You have already saved this event.')
		return HttpResponseRedirect(reverse('EventDetails:eventdetails', args=(pk,)))

@login_required 
@transaction.atomic
def rsvp(request, pk):
	theevent = get_object_or_404(Event, pk=pk)
	try:
		test = RSVPList.objects.get(Q(event_id=pk) & Q(user=request.user.get_username()))
	except (KeyError, RSVPList.DoesNotExist):
		theevent.rsvplist_set.create(user=request.user.get_username())
		return HttpResponseRedirect(reverse('EventDetails:eventdetails', args=(pk,)))
	else:
		#https://docs.djangoproject.com/en/1.9/ref/contrib/messages/
		messages.error(request, 'You have already RSVPd to this event.')
		return HttpResponseRedirect(reverse('EventDetails:eventdetails', args=(pk,)))

@login_required
@transaction.atomic
def vote(request, pk):
	theevent = get_object_or_404(Event, pk=pk)

	try:
		test = VoteList.objects.get(Q(event_id=pk) & Q(user=request.user.get_username()))
	except (KeyError, VoteList.DoesNotExist):
		theevent.votelist_set.create(user=request.user.get_username()) #update votes list
		
		theevent.votes += 1 #update the vote field in events
		theevent.save()     #for displaying most upvoted events
		
		return HttpResponseRedirect(reverse('EventDetails:eventdetails', args=(pk,)))
	else:
		messages.error(request, 'You have already voted for this event.')
		return HttpResponseRedirect(reverse('EventDetails:eventdetails', args=(pk,)))
		

#CUSTOM EVENTS VERSION OF RSVP & VOTE
@login_required 
@transaction.atomic
def customrsvp(request, pk):
	theevent = get_object_or_404(CustomEvent, pk=pk)
	try:
		test = RSVPCustomList.objects.get(Q(title=pk) & Q(user=request.user.get_username()))
	except (KeyError, RSVPCustomList.DoesNotExist):
		theevent.rsvpcustomlist_set.create(user=request.user.get_username())
		return HttpResponseRedirect(reverse('EventDetails:customeventdetails', args=(pk,)))
	else:
		#https://docs.djangoproject.com/en/1.9/ref/contrib/messages/
		messages.error(request, 'You have already RSVPd to this event.')
		return HttpResponseRedirect(reverse('EventDetails:customeventdetails', args=(pk,)))

@login_required
@transaction.atomic
def customvote(request, pk):
	theevent = get_object_or_404(CustomEvent, pk=pk)
	try:
		test = VoteCustomList.objects.get(Q(title=pk) & Q(user=request.user.get_username()))
	except (KeyError, VoteCustomList.DoesNotExist):
		theevent.votecustomlist_set.create(user=request.user.get_username()) #update votes list
		
		theevent.votes += 1 #update the vote field in events
		theevent.save()     #for displaying most upvoted events
		
		return HttpResponseRedirect(reverse('EventDetails:customeventdetails', args=(pk,)))
	else:
		messages.error(request, 'You have already voted for this event.')
		return HttpResponseRedirect(reverse('EventDetails:customeventdetails', args=(pk,)))
