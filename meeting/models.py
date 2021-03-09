from django.db import models
from datetime import datetime, date
# Create your models here.
class createMeeting(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    venue = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    start_time = models.TimeField(auto_now_add=False, auto_now=False, blank=True)
    end_time = models.TimeField(auto_now_add=False, auto_now=False, blank=True)

    class Meta:
        db_table = "meetingDB"
    
    def __str__(self):
        return self.title

class attendee(models.Model):
    title = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    attendance = models.BooleanField(default=False)

    class Meta:
        db_table = "attendeesDB"

    def __str__(self):
        return self.name

class addminutes(models.Model):
    titles = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    start_time = models.TimeField(auto_now_add=False, auto_now=False, blank=True)
    end_time = models.TimeField(auto_now_add=False, auto_now=False, blank=True)
    attendees_name = models.TextField()
    talking_points = models.TextField()
    action_items = models.TextField()

    class Meta:
        db_table = "minutesDB"

    def __str__(self):
        return self.titles