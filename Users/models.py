from django.db import models

# Create your models here.

from Auth.models import ILPUser

class Participant(models.Model):

	participant_id = models.OneToOneField(ILPUser)
	
	lg_id = models.ForeignKey('ILP.LG')
	
	
class Stream(model.Model):
	
	stream_id =  models.CharField(
		verbose_name = "Stream Id",
		unique = True,
		max_length = 50,
	)

	stream_name =  models.CharField(
		verbose_name = "Stream Name",
		max_length = 50,
	)

class Lead(model.Model):
	
	lead_id = models.OneToOneField(ILPUser)

    stream = models.ForeignKey('Stream')

class Department(model.Model):
	
	department_id =  models.CharField(
		verbose_name = "Department Id",
		unique = True,
		max_length = 50,
	)

	department_name =  models.CharField(
		verbose_name = "Department Name",
		max_length = 50,
	)

class Support(model.Model):

	support_id = models.OneToOneField(ILPUser)

	department_id =  models.ForeignKey('Stream')

class Guest(model.Model):
	
	guest_id = models.OneToOneField(ILPUser)

	sessions = models.ManyToManyField('Schedule.Session') 


