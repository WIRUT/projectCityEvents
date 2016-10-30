from django.conf.urls import url
from . import views

app_name = 'EventDetails'
urlpatterns = [
	url(r'^(?P<pk>.*)/eventinfo$', views.EventDetailsView, name='eventdetails'),
	url(r'^(?P<pk>.*)/rsvp$', views.rsvp, name='rsvp'),
	url(r'^(?P<pk>.*)/vote$', views.vote, name='vote'),
	url(r'^(?P<pk>.*)/saveEvent$', views.saveEvent, name='saveEvent'),
	url(r'^(?P<pk>.*)/customeventinfo$', views.CustomEventDetailsView, name='customeventdetails'),
	url(r'^(?P<pk>.*)/customrsvp$', views.customrsvp, name='customrsvp'),
	url(r'^(?P<pk>.*)/customvote$', views.customvote, name='customvote'),
]
