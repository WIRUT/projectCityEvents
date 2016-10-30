from django import forms
from django.forms.extras.widgets import SelectDateWidget
from django.forms.widgets import TextInput
from django_countries.fields import LazyTypedChoiceField
from django_countries import countries
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Div, MultiField
from crispy_forms.bootstrap import (FormActions)
# from .models import EventSearchModel

class EventSearchForm(forms.Form):

	search_keyword = forms.CharField( 
			max_length=200, 
			required=True, 
			widget=forms.TextInput(attrs={
				'value' : '',
				'placeholder' : 'Search by event name, venue, or performer...',
				'class': 'center-block col-lg-8'})) 
			#if I make this bigger (col-xs-24), the button gets misaligned

	search_city = forms.CharField(label='City (optional)',
			max_length=200, 
			required=False,
			widget=TextInput(attrs={
				'value': '',
				'placeholder': 'eg. Manchester',
				'class': 'col-xs-2'
				}))

	search_country = LazyTypedChoiceField(
			label='Country (optional)',
			choices=tuple([(u'', '(select a country)')] + list(countries)),#countries,
			required=False)

	search_from_date = forms.DateField(label='Search from date (optional)', 
			required=False,
			widget=TextInput(attrs={
				'id':'datepicker',
				'value': '',
				'placeholder': 'eg. MM/DD/YYYY'
				}))

	helper = FormHelper()
	helper.form_method = 'POST'
	helper.layout = Layout(Div(
	Div('search_keyword', css_class='center-block'), css_class ='form-group row'),
		Div(Div('search_city', css_class='search_city col-md-4'), Div('search_country', css_class='search_city2 col-md-4'),Div('search_from_date', css_class='search_from_date col-md-4'), css_class = 'form-group row'),
	FormActions(Submit('submit', 'search', css_class='btn btn-warning btn-secondary center-block')),
	)

	def clean(self):
		cleaned_data = super(EventSearchForm, self).clean()
		city = cleaned_data.get("search_city")
		country = cleaned_data.get("search_country")

		if country and not city:
			raise forms.ValidationError("Please select a city and country")
		if city and not country:
			raise forms.ValidationError("Please select a city and country")
