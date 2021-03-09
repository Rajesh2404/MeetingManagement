"""meeting_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.conf.urls import include
from meeting import views

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^meeting/', include('meeting.urls')),
    url(r'^home/', views.home, name='home'),
    url(r'^create_meeting/', views.create_meeting, name='create_meeting'),
    url(r'^minutes/', views.minutes, name='minutes'),
    url(r'^add_minutes/', views.add_minutes, name='add_minutes'),
    url(r'^attendees/', views.attendees, name='attendees'),
    url(r'^admin/', admin.site.urls),
]
