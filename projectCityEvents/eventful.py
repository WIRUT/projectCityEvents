class Eventful():
	app_key = '682VP5CCwMGh36K9'
	oauth_key = 'fbcd2dd23d72d1b7b965'
	oauth_secret = '1eea5c9cc672d44b8260'
	search_url_str = 'http://api.eventful.com/json/events/search?&app_key='
	keyword_query_str = '&keywords='
	images_sizes = '&image_sizes=small,medium,large'
	future_date = '&date=Future'
	price = '&include=price'
	page = '&page_number='
	city = '&location='
	date = '&date=' 

	def getSearchURL(self):
		return self.search_url_str + self.app_key + self.images_sizes + self.price + self.future_date + self.keyword_query_str

	def getPage(self):
		return self.page

	def getImageStr(self):
		return self.images_sizes

	def getAPPKey(self):
		return self.app_key

	def getOAuthKey(self):
		return self.oauth_key
	
	def getOAuthSecret(self):
		return self.oauth_secret

	def printURL(self):
		print getSearchURL()

	def getCity(self):
		return self.city

	def	getDate(self):
		return self.date
