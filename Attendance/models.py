from django.db import models

# Create your models here.

from Auth.models import ILPUser

class AttendanceLog(models.Model):
	
	participant_id = models.ForeignKey(ILPUser)

	session_id = models.ForeignKey('Schedule.Session', blank=True, null=True)

	extra_slot_id = models.ForeignKey('Schedule.ExtraSlot', blank=True, null=True)

	started_at = models.TimeField(
		verbose_name = "Time Slot Start Time",
	)
	
	ended_at = models.TimeField(
		verbose_name = "Time Slot End Time",
		null = True,
	)

