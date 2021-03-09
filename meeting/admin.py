from django.contrib import admin
from .models import createMeeting, addminutes, attendee
# Register your models here.
admin.site.register(createMeeting)
admin.site.register(addminutes)
admin.site.register(attendee)