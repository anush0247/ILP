from django.db import models

class LearingCenter(models.Model):
	
	center_id = models.CharField(
		verbose_name = "Learing Center Id",
		unique = True,
		max_length = 50,
	)

	center_name = 	models.CharField(
		verbose_name = "Learing Center Name",
		max_length = 50,
	)


class LearingCampus(models.Model) :

	campus_id = CharField(
		verbose_name = "Learing Campus Id",
		unique = True,
		max_length = 50,
	)

	campus_name = models.CharField(
		verbose_name = "Learing Campus Name",
		max_length = 50,
	)

	center = models.ForeignKey('LearingCenter')
	

class LearingRoom(models.Model) :

	room_id = models.CharField(
		verbose_name = "Learing Room Id",
		unique = True,
		max_length = 50,
	)

	room_name =  models.CharField(
		verbose_name = "Learing Room Name",
		max_length = 50,
	)

	room_location = models.ForeignKey('LearingCampus')

	campus = models.ForeignKey('LearingCampus')

class Batch(models.Model):

	batch_id = models.CharField(
		verbose_name = "Batch Id",
		unique = True,
		max_length = 50,
	)

	batch_name = models.CharField(
		verbose_name = "Batch Name",
		max_length = 50,
	)

	start_date = models.DateField(
		verbose_name = "Start Date",
	)

	end_date = model.DateField(
		verbose_name = "End Date",
	)
	
	center = models.ForeignKey('LearingCenter')

class LG(models.Model):

	lg_id = models.CharField(
		verbose_name = "Learing Group Id",
		unique = True,
		max_length = 50,
	)	

	lg_name = models.CharField(
		verbose_name = "Learing Group Name",
		max_length = 50,
	)	

	batch_id = models.ForeignKey('Batch')

	room_id = models.ForeignKey('LearingRoom')

class LG_Lead(models.Model):
	
	lg_id = model.ForeignKey('LG')

	lead_id = model.ForeignKey(ILPUser)

	start_date = models.DateField(
		verbose_name = "Start Date",
	)

	end_date = model.DateField(
		verbose_name = "End Date",
	)
	
