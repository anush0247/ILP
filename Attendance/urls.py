from django.conf.urls import patterns, include, url
from .views import AttendaceView, StartSession

urlpatterns = [
	url(r'^$', AttendaceView, name="attendance_home"),
	url(r'^start/(?P<session>\d{1,5})/$', StartSession, name="start_session"),
		
]
