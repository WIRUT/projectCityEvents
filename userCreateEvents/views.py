from django.shortcuts import render, redirect, get_object_or_404
from .forms import EventCreationForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import DeleteView 
from django.core.urlresolvers import reverse_lazy
from .models import CustomEvent

# Create your views here.
@login_required
def NewEvent(request):
    if request.method == "POST":
        form = EventCreationForm(request.POST,request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.searchtags = event.title + " " + event.performers + " " + event.venue_name + " " + event.city_name
            event.owner = request.user
            event.created_time = timezone.now()
            event.last_modified = timezone.now()
            event.eventphoto = form.cleaned_data['eventphoto']
            event.save()
            return redirect('event_success')
    else:
        form = EventCreationForm()
    return render(request, 'new_event.html', {'form': form})

@login_required
def EventList(request):
    eventlist = CustomEvent.objects.filter(owner=request.user)
    return render(request, 'eventlist.html', {'eventlist':eventlist})

@login_required
def EditEvent(request,pk):
    event = get_object_or_404(CustomEvent, pk=pk, owner=request.user)
    if request.method == "POST":
        form = EventCreationForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            # save the form into contact, where you can get the pk value
            event = form.save()

            return redirect('edit_success')
    else:
        form = EventCreationForm(instance=event)
    return render(request, 'edit_event.html', {'form':form})

@login_required
def DeleteEvent(request,pk):
    event = get_object_or_404(CustomEvent, pk=pk, owner=request.user)
    if request.method == "POST":
        event.delete()
        return redirect('Event_list')
    else:
        return redirect('/')


