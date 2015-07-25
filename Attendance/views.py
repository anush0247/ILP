from django.shortcuts import render

# importing login required decorator
from django.contrib.auth.decorators import login_required as auth
from django.contrib import messages
from django.conf import settings

from Users.models import Participant
from Schedule.models import Session, ExtraSlot
from Attendance.models import AttendanceLog
import datetime 

@auth
def AttendaceView(request):
	
	participant_profile = Participant.objects.get(participant_id = request.user)
	general_sessions = Session.objects.filter(lg_id = participant_profile.lg_id, date=datetime.date.today())
	extra_slots = ExtraSlot.objects.filter(participant_id=request.user,date=datetime.date.today() )
	context = {
		"participant_profile" : participant_profile ,
		"general_sessions": general_sessions,
		"extra_slots" : extra_slots,
	 }
	return render(request, "Attendance/home.html", context)


@auth
def StartSession(request, session):
	
	participant_profile = Participant.objects.get(participant_id = request.user)
	attendance_log = AttendanceLog.objects.filter(participant_id = request.user, session_id = Session.objects.get(id = session) )
	
	if(len(attendance_log) == 0 ):
		orinal = Session.objects.get(id = session).time_slot.start_time.hour*60 + Session.objects.get(id = session).time_slot.start_time.minute
		now = datetime.datetime.now().hour*60 + datetime.datetime.now().minute
		if( ( (now - orinal) <= settings.DUE_MINUTES )) :
			started_at = datetime.time(datetime.datetime.now().hour, datetime.datetime.now().minute)
			entry = AttendanceLog(participant_id = request.user,session_id = Session.objects.get(id = session), started_at = started_at )
			entry.save()
			messages.success(request,'Session #%s started at #%s' %(session, entry.id) )
		else :
			messages.error(request,'Not allowed to Start this Session #%s' %(session))
	else :
		messages.error(request,'Session #%s already started at #%s' %(session, attendance_log[0].id))
			

	general_sessions = Session.objects.filter(lg_id = participant_profile.lg_id, date=datetime.date.today())
	extra_slots = ExtraSlot.objects.filter(participant_id=request.user,date=datetime.date.today() )
	context = {
		"participant_profile" : participant_profile ,
		"general_sessions": general_sessions,
		"extra_slots" : extra_slots,
	 }
	return render(request, "Attendance/home.html", context)		

@auth
def StartExtraSlot(request, extra_slot_id ):
	pass

@auth
def StopSession(request, log_id ):
	pass

	
