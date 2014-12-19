from django.contrib import admin
from diary.models import *
# Register your models here.


@admin.register(Calender)
class CalenderAdmin(admin.ModelAdmin):
	list_display = ('name', 'owner', 'created', 'updated', 'priority', 'active', 'attr1', 'attr2')
	search_fields = ('name', 'owner')
	list_filter = ('owner', 'created', 'updated', 'active', 'attr1', 'attr2')
	date_heirarchy = 'updated'


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
	list_display = ('name', 'calender', 'start', 'end', 'created', 'updated', 'reminder', 'priority', 'active', 'attr1', 'attr2')
	search_fields = ('name', 'calender')
	list_filter = ('calender', 'start', 'end', 'created', 'updated', 'reminder', 'active', 'attr1', 'attr2')
	date_heirarchy = 'updated'


@admin.register(Day)
class DayAdmin(admin.ModelAdmin):
	list_display = ('date', 'owner', 'created', 'updated', 'attr1', 'attr2')
	search_fields = ('date', 'owner')
	list_filter = ('date', 'owner', 'created', 'updated', 'attr1', 'attr2')
	date_heirarchy = 'date'
