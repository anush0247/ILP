from django.contrib import admin

# Register your models here.

from Schedule.models import TimeSlot, Session, ExtraSlot

class TimeSlotAdmin(admin.ModelAdmin):
	list_display = ('slot_id','slot_name','start_time','end_time','is_break', 'campus')

admin.site.register(TimeSlot, TimeSlotAdmin)

class SessionAdmin(admin.ModelAdmin):
	list_display = ('session_id','session_name', 'incharge', 'lg_id', 'time_slot', 'date')

admin.site.register(Session, SessionAdmin)

class ExtraSlotAdmin(admin.ModelAdmin):
	list_display = ('participant_id', 'time_slot', 'date')

admin.site.register(ExtraSlot, ExtraSlotAdmin)
