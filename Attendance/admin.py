from django.contrib import admin
from Attendance.models import AttendanceLog

class AttendanceLogAdmin(admin.ModelAdmin):
	list_display = ('participant_id', 'session_id', 'extra_slot_id', 'started_at', 'ended_at')

admin.site.register(AttendanceLog, AttendanceLogAdmin)
