from django.db import models

# Create your models here.

from Auth.models import ILPUser

class TimeSlot(models.Model):
	
	slot_id = models.CharField(
		verbose_name = "Time Slot  Id",
		unique = True,
		max_length = 50,
	)

	slot_name = models.CharField(
		verbose_name = "Time Slot Name",
		max_length = 50,
	)

	start_time = models.TimeField(
		verbose_name = "Time Slot Start Time",
	)
	
	end_time = models.TimeField(
		verbose_name = "Time Slot End Time",
	)
	
	is_break = models.BooleanField(
        default=False,
        verbose_name = "Is a Break ?",
    )
	
	campus =  models.ForeignKey('ILP.LearingCampus')
	
	def __unicode__(self):
        return unicode(self.slot_id)


class Session(models.Model):
	
	session_id =  models.CharField(
		verbose_name = "Schedule Id",
		unique = True,
		max_length = 50,
	)

	session_name = models.CharField(
		verbose_name = "Schedule Name",
		max_length = 50,
	)

	incharge = models.ManyToManyField(ILPUser)

	lg_id = models.ForeignKey('ILP.LG')

	time_slot = models.ForeignKey('TimeSlot')

	date = models.DateField(
        verbose_name = "Date",
    )	

	def __unicode__(self):
        return unicode(self.session_id)

class ExtraSlot(models.Model):
	
	participant_id = models.ForeignKey(ILPUser)

	time_slot = models.ForeignKey('TimeSlot')

	date = date = models.DateField(
        verbose_name = "Date",
    )
	
	

