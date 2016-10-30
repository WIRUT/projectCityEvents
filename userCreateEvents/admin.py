from django.contrib import admin

# Register your models here.
from .models import CustomEvent

admin.site.register(CustomEvent)