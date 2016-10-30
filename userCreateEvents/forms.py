from django import forms
from django.db import models
from .models import CustomEvent
from crispy_forms.helper import FormHelper
from django.forms.widgets import TextInput
from crispy_forms.layout import Submit, Layout, Field, Div, MultiField
from crispy_forms.bootstrap import (
    PrependedText, PrependedAppendedText, FormActions)
from datetimewidget.widgets import DateTimeWidget
from django.utils.translation import ugettext_lazy as _



class EventCreationForm(forms.ModelForm):


# TODO: Start time and end time need actual hours instead of dates. MIght need additional fields possibly
# might need to include  picture!!!!

	# venue_name = forms.CharField(label="Venue")
	# address = forms.CharField
	class Meta:

		model = CustomEvent
		fields = ['title','performers','description',
		'venue_name', 'price','ticket_URL', 'start_time', 'stop_time', 'eventphoto', 'address',
		'country_name','city_name','region_name','longitude','latitude']


		widgets = {
           'start_time': DateTimeWidget(attrs={'id':"yourdatetimeid"}, usel10n = True, bootstrap_version=3),
           'stop_time': DateTimeWidget(attrs={'id':"yourdatetimeid2"}, usel10n = True, bootstrap_version=3),

        }
# NOT WORKING
        # labels = {
        # 	'venue_name': 'Venue',
        # 	'start_time': "Start",
        # 	'stop_time': "End",
        # 	'eventphoto': "Event Photo",
        # 	'address': "Address selected below:",
        # 	'country_name': "country",
        # 	'city_name': "city",
        # 	'region_name': "Province/Region", 
        # }

	helper = FormHelper()
	helper.form_method = 'POST'
	helper.layout = Layout(Div(
	'title','performers','description','eventphoto', css_class ="col-md-3"),
		Div('city_name', 'region_name','country_name', PrependedText('price', '$'),
		'ticket_URL', 'start_time', 'stop_time',  css_class = "col-md-3"),
		Div('venue_name',Field('address', readonly=True),Div(css_id="map"),Field('latitude', type='hidden'), Field('longitude', type='hidden'), css_class="col-md-6"),
	FormActions(Submit('submit', 'submit', css_class='btn-primary')),
	)




