from django.db import models

# Create your models here.

from Auth.models import ILPUser

class Participant(models.Model):

	participant_id = models.OneToOneField(ILPUser)
	
	lg_id = models.ForeignKey('ILP.LG')

	def __unicode__(self):
		return unicode(self.participant_id)
	
	
class Stream(models.Model):
	
	
	stream_name =  models.CharField(
		verbose_name = "Stream Name",
		max_length = 50,
	)
	
	def __unicode__(self):
		return unicode(self.stream_name)

class Lead(models.Model):
	
	lead_id = models.OneToOneField(ILPUser)
	
	stream = models.ForeignKey('Stream')

	def __unicode__(self):
		return unicode(self.lead_id)

class Department(models.Model):
	
	

	department_name =  models.CharField(
		verbose_name = "Department Name",
		max_length = 50,
	)

	def __unicode__(self):
		return unicode(self.department_name)

class Support(models.Model):

	support_id = models.OneToOneField(ILPUser)

	department_id =  models.ForeignKey('Stream')

	designation = models.CharField(
		verbose_name = "Designation",
		max_length = 50,
	)

	def __unicode__(self):
		return unicode(self.support_id)

class Guest(models.Model):
	
	guest_id = models.OneToOneField(ILPUser)

	sessions = models.ManyToManyField('Schedule.Session') 

	def __unicode__(self):
		return unicode(self.guest_id)


