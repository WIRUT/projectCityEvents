from django.conf.urls import url, patterns
from django.contrib import admin
from . import views

app_name='dashboard'
urlpatterns = [
	url(r'^(?P<search_key>.*)/results/(?P<page>.*)$', views.results, name='results'),
	url(r'^(?P<search>.*)/showMore/(?P<pageNo>.*)$', views.showMore, name='showMore'),
	url(r'^admin/', admin.site.urls),
]