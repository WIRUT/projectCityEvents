from django.conf.urls import url
from . import views

app_name = 'saveEvents'
urlpatterns = [
	url(r'^userSavedEvents$', views.userSavedEvents, name='userSavedEvents'),
	url(r'^(?P<pk>.*)/deleteEvent$', views.deleteEvent, name='deleteEvent'),
]