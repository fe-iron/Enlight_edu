from django.contrib import admin
from .models import News, UpcomingEvent

# Register your models here.

admin.site.register(News)

admin.site.register(UpcomingEvent)