from django.contrib import admin

# Register your models here.

from Users.models import Participant, Stream, Lead, Department, Support, Guest

class ParticipantAdmin(admin.ModelAdmin):
	list_display = ('participant_id','lg_id')

admin.site.register(Participant, ParticipantAdmin)

class StreamAdmin(admin.ModelAdmin):
	list_display = ('stream_id', 'stream_name')

admin.site.register(Stream, StreamAdmin)

class LeadAdmin(admin.ModelAdmin):
	list_display = ('lead_id', 'stream')

admin.site.register(Lead, LeadAdmin)

class DepartmentAdmin(admin.ModelAdmin):
	list_display = ('department_id', 'department_name')

admin.site.register(Department, DepartmentAdmin)

class SupportAdmin(admin.ModelAdmin):
	list_display = ('support_id', 'department_id','designation')

admin.site.register(Support, SupportAdmin)

class GuestAdmin(admin.ModelAdmin):
	list_display = ('guest_id',)

admin.site.register(Guest, GuestAdmin)
