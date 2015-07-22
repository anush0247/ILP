from django.contrib import admin

from ILP.models import LearningCenter, LearningCampus, LearningRoom, Batch, LG, LG_Lead

class LearningCenterAdmin(admin.ModelAdmin):
	list_display = ('center_id','center_name')

admin.site.register(LearningCenter, LearningCenterAdmin)

class LearningCampusAdmin(admin.ModelAdmin):
	list_display = ('campus_id', 'campus_name', 'center')

admin.site.register(LearningCampus, LearningCampusAdmin)

class LearningRoomAdmin(admin.ModelAdmin):
	list_display = ('room_id', 'room_name', 'room_location', 'campus')

admin.site.register(LearingRoom, LearningRoomAdmin)

class BatchAdmin(admin.ModelAdmin):
	list_display = ('batch_id', 'batch_name', 'start_date', 'end_date', 'center')

admin.site.register(Batch, BatchAdmin)

class LGAdmin(admin.ModelAdmin):
	list_display = ('lg_id','lg_name', 'batch_id','room_id')

admin.site.register(LG, LGAdmin)

class LG_LeadAdmin(admin.ModelAdmin):
	list_display = ('lg_id', 'lead_id', 'start_date', 'end_date')

admin.site.register(LG_Lead, LG_LeadAdmin)
