from django.contrib import admin
from .models import Employee,Scheduleemployee

@admin.register(Employee)
class AdminEmployee(admin.ModelAdmin):
	list_display = ('userprofile', 'celphone', 'phone','position',)
	list_filter = ('userprofile','position',)

@admin.register(Scheduleemployee)
class AdminScheduleemployee(admin.ModelAdmin):
	list_display = ('employee','day','entryTime','departureTime',)
	list_filter = ('employee',)
