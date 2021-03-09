from django import forms
#from django.contrib.auth.models import User
from meeting.models import createMeeting, addminutes, attendee


class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'
    
    
class createMeetingForm(forms.ModelForm):
    class Meta:
        model = createMeeting
        fields = ['title','description','venue','date','start_time','end_time']


        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-style', 'autocomplete': 'off', 'required': '', 'placeholder': 'Meeting Title'}),
            'description' : forms.Textarea(attrs={'class': 'form-style', 'rows':'5', 'autocomplete': 'off', 'required': '', 'placeholder': 'Description'}),
            'venue' : forms.TextInput(attrs={'class': 'form-style', 'autocomplete': 'off', 'required': '', 'placeholder': 'Venue'}),
            'date' : DateInput(attrs={'class': 'form-style', 'autocomplete': 'off', 'required': '', 'placeholder': 'Date'}),
            'start_time' : TimeInput(attrs={ 'class': 'form-style', 'autocomplete': 'off', 'required': '', 'placeholder': 'Start Time'}),
            'end_time' : TimeInput(attrs={'class': 'form-style', 'autocomplete': 'off', 'required': '', 'placeholder': 'End Time'})
        }

class attendeeForm(forms.ModelForm):
    class Meta:
        model = attendee
        fields = ['title','name','email','attendance']


        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-style', 'autocomplete': 'off', 'required': '', 'placeholder': 'Title'}),
            'name' : forms.TextInput(attrs={'class': 'form-style', 'autocomplete': 'off', 'required': '', 'placeholder': 'Name'}),
            'email' : forms.TextInput(attrs={'class': 'form-style', 'autocomplete': 'off', 'required': '', 'placeholder': 'Email'}),
            'attendance' : forms.BooleanField()
        }

class addminutesForm(forms.ModelForm):
    class Meta:
        model = addminutes
        fields = ['titles','date', 'start_time', 'end_time', 'attendees_name','talking_points','action_items']


        widgets = {
            'titles' : forms.TextInput(attrs={'class': 'form-style', 'autocomplete': 'off', 'required': '', 'placeholder': 'Meeting Title'}),
            'date' : DateInput(attrs={'class': 'form-style', 'autocomplete': 'off', 'required': '', 'placeholder': 'Date'}),
            'start_time' : TimeInput(attrs={ 'class': 'form-style', 'autocomplete': 'off', 'required': '', 'placeholder': 'Start Time'}),
            'end_time' : TimeInput(attrs={'class': 'form-style', 'autocomplete': 'off', 'required': '', 'placeholder': 'End Time'}),
            'attendees_name' : forms.Textarea(attrs={'class': 'form-style', 'rows':'4', 'autocomplete': 'off', 'required': '', 'placeholder': 'Attendees'}),
            'talking_points' : forms.Textarea(attrs={'class': 'form-style', 'rows':'4', 'autocomplete': 'off', 'required': '', 'placeholder': 'Talking Points'}),
            'action_items' : forms.Textarea(attrs={'class': 'form-style', 'rows':'4', 'autocomplete': 'off', 'required': '', 'placeholder': 'Action Items'}),
        }
