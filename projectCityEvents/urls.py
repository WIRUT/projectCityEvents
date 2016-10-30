"""projectCityEvents URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView
from accounts import views
import allauth
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    url(r'', include('dashboard.urls')),
    url(r'', include('eventSearch.urls')),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',{'next_page': '/logged_out/'}, name= "logout"),
    url(r'^logged_out/$', views.logged_out),
    url(r'^accounts/(?P<pk>[0-9]+)/$', views.edit_user, name= "edit_user"),
    url(r'^signup/$', views.signup, name="signup"),
    url(r'^$', TemplateView.as_view(template_name='base.html'), name="home"),
	url(r'', include('EventDetails.urls')),
    url(r'', include('userCreateEvents.urls')),
    url(r'', include('saveEvents.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
