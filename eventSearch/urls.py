from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.Eventful_Search, name='Eventful_Search'),
]
