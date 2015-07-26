from django.shortcuts import render
from django.http import Http404

# importing login required decorator
from django.contrib.auth.decorators import login_required as auth
from django.contrib import messages
from django.conf import settings

from Users.models import Participant
from Schedule.models import Session, ExtraSlot
from Attendance.models import AttendanceLog
import datetime 

def get_all_sessions_info(request, model, prefix ):

	participant_profile = Participant.objects.get(participant_id = request.user)

	_slots = None

	if(prefix == "session") :
		_slots = Session.objects.filter(lg_id = participant_profile.lg_id, date=datetime.date.today())
	else :
		_slots = ExtraSlot.objects.filter(participant_id=request.user,date=datetime.date.today()) 

	_list = []

	for _slot in _slots:
		
		_dict = {}
		_dict[prefix] = _slot
		
		_start = None
		if(prefix == "session") :
			_start = AttendanceLog.objects.filter(participant_id = request.user, session_id = model.objects.get(id = _slot.id))
		else :
			_start = AttendanceLog.objects.filter(participant_id = request.user, extra_slot_id = model.objects.get(id = _slot.id) )

		started_flag = "Yet to Start"
		stop_flag = "You missed"
		started_log = None

		
		
		if(len(_start) == 0) :

			now = datetime.datetime.now().hour*60 + datetime.datetime.now().minute
			orinal_start = model.objects.get(id = _slot.id).time_slot.start_time.hour*60 + model.objects.get(id = _slot.id).time_slot.start_time.minute
			diff = now - orinal_start

			if diff <= settings.DUE_MINUTES and  diff >= 0  :
				started_flag = "Start"
				stop_flag = "Yet to Stop"
			elif ( diff < 0 ) :
				started_flag = "Yet to Start"
			else :
				started_flag = "You missed"
		else :
			started_log = _start[0]
			started_flag = "Already Started"
			if(_start[0].ended_at != None ):
				stopped_at = _start[0].ended_at
				stop_flag = "Stopped"
			else :
				
				now = datetime.datetime.now().hour*60 + datetime.datetime.now().minute
				orinal_stop = model.objects.get(id = _slot.id).time_slot.end_time.hour*60 + model.objects.get(id = _slot.id).time_slot.end_time.minute
				diff = now - orinal_stop
				if  diff <= settings.DUE_MINUTES  and diff >= 0  :
					stop_flag = "Stop"
				elif ( diff < 0 ) :
					stop_flag = "Yet to Stop"
				else :
					stop_flag = "You missed"
				

		_dict["started_log"] = started_log
		_dict["started_flag"] = started_flag
		_dict["stop_flag"] = stop_flag

		_list.append(_dict)
	
	return _list

def get_attendance_context(request):
	
	participant_profile = Participant.objects.get(participant_id = request.user)
	general_sessions = Session.objects.filter(lg_id = participant_profile.lg_id, date=datetime.date.today())
	extra_slots = ExtraSlot.objects.filter(participant_id=request.user,date=datetime.date.today()) 
	
	context = {
		"participant_profile" : participant_profile ,
		"general_sessions": get_all_sessions_info(request,Session, "session" ),
		"extra_slots" : get_all_sessions_info(request, ExtraSlot, "extra_slot" ),
	 }
	
	return context

@auth
def AttendaceView(request):
	return render(request, "Attendance/home.html", get_attendance_context(request))


@auth
def StartSession(request, session):

	try :
		Session.objects.get(id = session, date=datetime.date.today())
	except Session.DoesNotExist:
		raise Http404("Invalid date & Session Combination")

	session_name = Session.objects.get(id = session, date=datetime.date.today()).session_name
	attendance_log = AttendanceLog.objects.filter(participant_id = request.user, session_id = Session.objects.get(id = session) )	
	if(len(attendance_log) == 0 ):
		orinal = Session.objects.get(id = session).time_slot.start_time.hour*60 + Session.objects.get(id = session).time_slot.start_time.minute
		now = datetime.datetime.now().hour*60 + datetime.datetime.now().minute
		if( ( (now - orinal) <= settings.DUE_MINUTES )) :
			started_at = datetime.time(datetime.datetime.now().hour, datetime.datetime.now().minute)
			entry = AttendanceLog(participant_id = request.user,session_id = Session.objects.get(id = session), started_at = started_at )
			entry.save()
			messages.success(request,'Session \'#%s\' started at #%s' %(session_name, entry.id) )
		else :
			messages.error(request,'Not allowed to Start this Session \'#%s\'' %(session_name))
	else :
		messages.error(request,'Session \'#%s\' already started at #%s' %(session_name, attendance_log[0].id))
		
	return render(request, "Attendance/home.html", get_attendance_context(request))	
	
		

@auth
def StartExtraSlot(request, extra_slot_id ):
	pass

@auth
def StopSession(request, log_id ):
	pass


	
