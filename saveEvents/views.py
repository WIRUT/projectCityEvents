from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import *
from django.contrib.auth.decorators import login_required

@login_required
def userSavedEvents(request):
	events = savedEvents.objects.filter(user=request.user.get_username())
	return render(request, 'saveEvents/saved_events.html', {'events':events})

@login_required
def deleteEvent(request, pk):
	eventToDelete = savedEvents.objects.get(pk=pk)
	eventToDelete.delete()
	return HttpResponseRedirect(reverse('saveEvents:userSavedEvents'))