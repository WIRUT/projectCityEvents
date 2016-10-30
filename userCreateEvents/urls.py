from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from . import views


urlpatterns = [
	url(r'^newevent/$', views.NewEvent, name='New_event'),
	url(r'^manageevents/$', views.EventList, name='Event_list'),
	url(r'^editevent/(?P<pk>[0-9]+)/$', views.EditEvent, name='Edit_event'),
	url(r'^deleteevent/(?P<pk>[0-9]+)/$', views.DeleteEvent, name='Delete_event'),
	url(r'^deleteeventconfirm/(?P<pk>[0-9]+)/$', TemplateView.as_view(template_name='delete_event_confirm.html'), name='Delete_event_confirm'),
	url(r'^manageevents/editeventsuccess/$', TemplateView.as_view(template_name='edit_event_success.html'), name='edit_success'),
	url(r'^manageevents/createsuccess/$', TemplateView.as_view(template_name='event_creation_success.html'), name='event_success'),
	url(r'^my_admin/jsi18n', 'django.views.i18n.javascript_catalog'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # remove this when in production



