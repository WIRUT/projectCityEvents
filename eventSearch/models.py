from django.db import models
from django.utils import timezone

class Performer(models.Model):
	name 	 		 = models.CharField(max_length=200, null=True) 
	url	 			 = models.URLField(null=True)
	performerID	 	 = models.CharField(max_length=200, null=True)
	bio  			 = models.TextField(null=True) 
	last_modified	 = models.DateTimeField(null=True) 

	def __str__(self):
		return self.name

	def getID(self):
		return self.performerID

	def getURL(self):
		return self.url

	def getBio(self):
		return self.bio

	def getLastModified(self):
		return self.last_modified	

class Venue(models.Model):
	venueID			 = models.CharField(max_length=50)
	name		 	 = models.CharField(max_length=100) 
	url				 = models.URLField(null=True, blank=True)
	latitude	 	 = models.DecimalField(decimal_places=9, max_digits=20, null=True)
	longitude		 = models.DecimalField(decimal_places=9, max_digits=20, null=True)
	address	 		 = models.CharField(max_length=200, null=True) 
	city			 = models.TextField(null=True)
	description		 = models.TextField(null=True, blank=True)
	facebook		 = models.URLField(null=True, blank=True)
	twitter			 = models.URLField(null=True, blank=True)
	website			 = models.URLField(null=True, blank=True)
	last_modified	 = models.DateTimeField(null=True)
	#event			 = models.ForeignKey(Event, on_delete=models.CASCADE,null=True)

	def __str__(self):
		return self.name

	def getID(self):
		return self.venueID

	def getName(self):
		return self.name	 

	def getLongitude(self):
		return self.longitude

	def getLatitude(self):
		return self.latitude

	def getCity(self):
		return self.city

	def getFacebook(self):
		return self.facebook

	def getTwitter(self):
		return self.twitter

	def getWebsite(self):
		return self.website

	def getDescription(self):
		return self.description

	def getEventfulURL(self):
		return self.url		

	def getAddress(self):
		return self.address

	def getLastModified(self):
		return self.last_modified
			
class Event(models.Model):
	title			 = models.CharField(max_length=200)
	eventID		  	 = models.CharField(max_length=200, null=True)
	performers		 = models.ManyToManyField(Performer)
	venue 			 = models.ForeignKey(Venue, null=True)
	description 	 = models.TextField(null=True)
	url				 = models.URLField(null=True, blank=True)
	votes			 = models.PositiveIntegerField(default=0, null=True)
	owner			 = models.CharField(max_length=100, null=True) 
	region_abbr	 	 = models.CharField(max_length=2, null=True) 
	region_name	 	 = models.CharField(max_length=50, null=True) 
	city_name	 	 = models.CharField(max_length=60, null=True)
	postal_code	 	 = models.CharField(max_length=8, null=True, blank=True)
	country_name	 = models.CharField(max_length=50, null=True) 
	country_abbr	 = models.CharField(max_length=3, null=True) 
	latitude	 	 = models.DecimalField(decimal_places=9, max_digits=20, null=True)
	longitude		 = models.DecimalField(decimal_places=9, max_digits=20, null=True)
	geocode_type	 = models.CharField(max_length=20, null=True, blank=True) 
	start_time	 	 = models.DateTimeField()
	stop_time		 = models.DateTimeField(null=True, blank=True)
	created_time	 = models.DateTimeField()
	last_modified	 = models.DateTimeField(null=True, blank=True) 
	spotifyURL		 = models.CharField(max_length=200, null=True)
	price			 = models.CharField(null=True, max_length=25)
	searchtags		 = models.CharField(max_length=1000, null=True)

	def __str__(self):
		return self.title

	def getLatitude(self):
		return self.latitude	 	 

	def getLongitude(self):
		return self.longitude

	def getPostalCode(self):
		return self.postal_code	  

	def getRegionAbbr(self):
		return self.region_abbr	 

	def getEventURL(self):
		return self.eventful_url	 

	def getEventID(self):
		return self.eventID			

	def getCity(self):
		return self.city_name	 	 

	def getCountry(self):
		return self.country_name	

	def getCountryAbbr(self):
		return self.country_abbr	 

	def getRegion(self):
		return self.region_name

	def getStartTime(self):
		return self.start_time	

	def getDescription(self):
		return self.description 	 

	def getLastModified(self):
		return self.last_modified	 

	def getEventCreator(self):
		return self.creator		 

	def getEventTitle(self):
		return self.title			 

	def getGeocodeType(self):
		return self.geocode_type	 

	def getEventOwner(self):
		return self.owner			 

	def getNumOfVotes(self):
		return self.votes

	def getDateTimeEventCreated(self):
		return self.created_time

	def getDateTimeEventStop(self):
		return self.stop_time	
	def getNewEvents(self):
		return self.created_time >= timezone.now() - datetime.timedelta(days=3)
	

class Image(models.Model):
	# width_thmb 	 	 = models.PositiveSmallIntegerField(null=True) 
	# height_thmb  	 = models.PositiveSmallIntegerField(null=True) 
	# url_thmb	 	 = models.URLField(null=True, blank=True)
	# width_sm	 	 = models.PositiveSmallIntegerField(null=True) 
	# height_sm	 	 = models.PositiveSmallIntegerField(null=True) 
	# url_sm	 	 	 = models.URLField(null=True, blank=True) 
	width_med	 	 = models.PositiveSmallIntegerField(null=True) 
	height_med 	 	 = models.PositiveSmallIntegerField(null=True) 
	url_med	 	 	 = models.URLField(null=True, blank=True)
	width_lg	 	 = models.PositiveSmallIntegerField(null=True) 
	height_lg	 	 = models.PositiveSmallIntegerField(null=True) 
	url_lg	 	 	 = models.URLField(null=True, blank=True) 
	last_modified	 = models.DateTimeField(null=True) 
	whatisthis		 = models.CharField(max_length=200, null=True)
	event			 = models.ForeignKey(Event, on_delete=models.CASCADE,null=True)

	def __str__(self):
		return 'Image'
	
	def getImgWidth(self):
		return self.width	 	 

	def getImgURL(self):
		return self.url	 	

	def getImgHeight(self):
		return self.height

	def getImgWidthSmall(self):
		return self.width_sm	 

	def getImgURLSmall(self):
		return self.url_sm

	def getImgHeightSmall(self):
		return self.height_sm	 

	def getImgWidthMed(self):
		return self.width_med	 

	def getImgURLMed(self):
		return self.url_med	 

	def getImgHeightMed(self):
		return self.height_med 

	def getImgWidthLg(self):
		return self.width_thmb	 

	def getImgURLLg(self):
		return self.url_thmb

	def getImgHeightLg(self):
		return self.height_thmb 

	def getLastModified(self):
		return self.last_modified	 