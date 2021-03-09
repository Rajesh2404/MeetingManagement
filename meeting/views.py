from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings

from meeting.models import createMeeting, addminutes, attendee
from meeting.forms import createMeetingForm, addminutesForm, attendeeForm

# Create your views here.
def index(request):
    meetings = createMeeting.objects.all().order_by('date','start_time')
    return render(request, 'meeting_app/index.html', {'meetings': meetings})
def home(request):
    return render(request, 'meeting_app/home.html')
def create_meeting(request):
    form = createMeetingForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            try:
                form.save()
                return redirect('meeting_app/create_meeting')
            except:
                pass
        else:
            form = createMeetingForm()
    return render(request, 'meeting_app/create_meeting.html', {'form':form})
def attendees(request):
    users = attendee.objects.all()
    #meetings = createMeeting.objects.all()
    form = attendeeForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            try:
                form.save()
                return redirect('meeting_app/attendees')
            except:
                pass
        else:
            form = attendeeForm()
    context = {'users': users, 'form': form}
    '''if users.title == meetings.title:
        name = users.name
        mailerID = users.email
        message = 'A meeting has been scheduled on ' + meetings.date + ' from ' + meetings.start_time + ' to ' + meetings.end_time + ' on ' + meetings.title
        send_mail('Contact form',
        'Hi Mr. ' + name + ', message: ' + message,
        settings.EMAIL_HOST_USER,
        [mailerID],
        fail_silently=False)'''
    return render(request, 'meeting_app/attendees.html', context)
def add_minutes(request):
    forms = addminutesForm(request.POST)
    if request.method == "POST":
        if forms.is_valid():
            try:
                forms.save()
                return redirect('meeting_app/add_minutes')
            except:
                pass
        else:
            forms = addminutesForm()
    return render(request, 'meeting_app/add_minutes.html', {'forms':forms})
def minutes(request):
    minute = addminutes.objects.all()
    return render(request, 'meeting_app/minutes.html', {'minute': minute})
