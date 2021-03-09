from django.conf.urls import url
from meeting import views

app_name = 'meeting_app'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home/', views.home, name='home'),
    url(r'^create_meeting/', views.create_meeting, name='create_meeting'),
    url(r'^minutes/', views.minutes, name='minutes'),
    url(r'^add_minutes/', views.add_minutes, name='add_minutes'),
    url(r'^attendees/', views.attendees, name='attendees'),
    
]