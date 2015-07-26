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

def start_session(request, model, prefix, pk ):
	try :
		model.objects.get(id = pk, date=datetime.date.today())
	except model.DoesNotExist:
		raise Http404("Invalid date & Session Combination")

	_name = ""
	if(prefix == "session"):
		_name = model.objects.get(id = pk, date=datetime.date.today()).session_name
	else :
		_name = model.objects.get(id = pk, date = datetime.date.today()).time_slot.slot_name

	_start = None
	if(prefix == "session") :
		_start = AttendanceLog.objects.filter(participant_id = request.user, session_id = model.objects.get(id = pk))
	else :
		_start = AttendanceLog.objects.filter(participant_id = request.user, extra_slot_id = model.objects.get(id = pk) )
	
	if(len(_start) == 0) :

		now = datetime.datetime.now().hour*60 + datetime.datetime.now().minute
		orinal_start = model.objects.get(id = pk).time_slot.start_time.hour*60 + model.objects.get(id = pk).time_slot.start_time.minute
		diff = now - orinal_start

		if diff <= settings.DUE_MINUTES and  diff >= 0  :
			started_at = datetime.time(datetime.datetime.now().hour, datetime.datetime.now().minute)
			if(prefix == "session") :
				entry = AttendanceLog(participant_id = request.user, session_id = model.objects.get(id = pk), started_at = started_at )
				entry.save()
				messages.success(request,'Session \'#%s\' started at #%s' %(_name, entry.id) )
			else :
				entry = AttendanceLog(participant_id = request.user, extra_slot_id = model.objects.get(id = pk), started_at = started_at )
				entry.save()
				messages.success(request,'Extra Slot \'#%s\' started at #%s' %(_name, entry.id) )
				
		elif ( diff < 0 ) :
			messages.error(request,'Not allowed to Start this Session / Extra Slot \'#%s\'' %(_name))
		else :
			messages.error(request,'Sorry.! You just missed to Start this Session / Extra Slot \'#%s\'' %(_name))
	else :
		messages.error(request,'Session / Extra Slot \'#%s\' already started at #%s' %(_name, _start[0].id))
	
	return render(request, "Attendance/home.html", get_attendance_context(request))	

def stop_session(request, model, prefix, pk ):
	try :
		model.objects.get(id = pk, date=datetime.date.today())
	except model.DoesNotExist:
		raise Http404("Invalid date & Session Combination")

	_name = ""
	if(prefix == "session"):
		_name = model.objects.get(id = pk, date=datetime.date.today()).session_name
	else :
		_name = model.objects.get(id = pk, date = datetime.date.today()).time_slot.slot_name

	_start = None
	if(prefix == "session") :
		_start = AttendanceLog.objects.filter(participant_id = request.user, session_id = model.objects.get(id = pk))
	else :
		_start = AttendanceLog.objects.filter(participant_id = request.user, extra_slot_id = model.objects.get(id = pk) )
	
	if(len(_start) != 0) :
		if(_start[0].ended_at == None) :
			now = datetime.datetime.now().hour*60 + datetime.datetime.now().minute
			orinal_start = model.objects.get(id = pk).time_slot.end_time.hour*60 + model.objects.get(id = pk).time_slot.end_time.minute
			diff = now - orinal_start

			if diff <= settings.DUE_MINUTES and  diff >= 0  :
				stopped_at = datetime.time(datetime.datetime.now().hour, datetime.datetime.now().minute)
				_start[0].ended_at = stopped_at
				_start[0].save()
				messages.success(request,'Session / Extra Slot \'#%s\' Stopped at #%s' %(_name, _start[0].ended_at) )	
			elif ( diff < 0 ) :
					messages.error(request,'Not allowed to Start this Session / Extra Slot \'#%s\'' %(_name))
			else :
					messages.error(request,'Sorry.! You just missed to Start this Session / Extra Slot \'#%s\'' %(_name))
		else :
			messages.error(request,'Session / Extra Slot \'#%s\' already started at #%s' %(_name, _start[0].id))
	else :
		messages.error(request,'Session / Extra Slot \'#%s\' Not yet Started. Please Start it first' %(_name))
	
	return render(request, "Attendance/home.html", get_attendance_context(request))	

@auth
def AttendaceView(request):
	return render(request, "Attendance/home.html", get_attendance_context(request))

@auth
def StartSession(request, session):
	return start_session(request, Session, "session", session )	

@auth
def StartExtraSlot(request, extra_slot_id ):
	return start_session(request, ExtraSlot, "extra_slot", extra_slot_id )

@auth
def StopSession(request, session ):
	return stop_session(request, Session, "session", session )	

@auth
def StopExtraSlot(request, extra_slot_id ):
	return stop_session(request, ExtraSlot, "extra_slot", extra_slot_id )


	
