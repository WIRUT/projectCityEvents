from __future__ import unicode_literals

from django.apps import AppConfig


class UsercreateeventsConfig(AppConfig):
    name = 'userCreateEvents'
    def ready(self):
    	import userCreateEvents.signals
 