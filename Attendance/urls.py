from django.conf.urls import patterns, include, url
from .views import AttendaceView, StartSession, StartExtraSlot, StopSession, StopExtraSlot

urlpatterns = [
	url(r'^$', AttendaceView, name="attendance_home"),
	url(r'^start/(?P<session>\d{1,5})/$', StartSession, name="start_session"),
	url(r'^start_extra/(?P<extra_slot_id>\d{1,5})/$', StartExtraSlot, name="start_extra_slot"),
	url(r'^stop/(?P<session>\d{1,5})/$', StopSession, name="stop_session"),
	url(r'^stop_extra/(?P<extra_slot_id>\d{1,5})/$', StopExtraSlot, name="stop_extra_slot"),		
]
