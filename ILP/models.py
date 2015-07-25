from django.db import models

class LearningCenter(models.Model):
	
	

	center_name = 	models.CharField(
		verbose_name = "Learing Center Name",
		max_length = 50,
	)


	def __unicode__(self):
		return unicode(self.center_name)

class LearningCampus(models.Model) :

	

	campus_name = models.CharField(
		verbose_name = "Learing Campus Name",
		max_length = 50,
	)

	center = models.ForeignKey('LearningCenter')

	def __unicode__(self):
		return unicode(self.campus_name)
	

class LearningRoom(models.Model) :

	room_id = models.CharField(
		verbose_name = "Learing Room Id",
		unique = True,
		max_length = 50,
	)

	room_name =  models.CharField(
		verbose_name = "Learing Room Name",
		max_length = 50,
	)

	room_location = models.ForeignKey('LearningCampus')

	def __unicode__(self):
		return unicode(self.room_name)

class Batch(models.Model):

	

	batch_name = models.CharField(
		verbose_name = "Batch Name",
		max_length = 50,
	)

	start_date = models.DateField(
		verbose_name = "Start Date",
	)

	end_date = models.DateField(
		verbose_name = "End Date",
	)
	
	center = models.ForeignKey('LearningCenter')

	def __unicode__(self):
		return unicode(self.batch_name)

class LG(models.Model):

	

	lg_name = models.CharField(
		verbose_name = "Learing Group Name",
		max_length = 50,
	)	

	batch_id = models.ForeignKey('Batch')

	room_id = models.ForeignKey('LearningRoom')

	def __unicode__(self):
		return unicode(self.lg_name)


class LG_Lead(models.Model):
	
	lg_id = models.ForeignKey('LG')

	lead_id = models.ForeignKey('Auth.ILPUser')

	start_date = models.DateField(
		verbose_name = "Start Date",
	)

	end_date = models.DateField(
		verbose_name = "End Date",
	)
	
