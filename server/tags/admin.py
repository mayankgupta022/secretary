from django.contrib import admin
from tags.models import *
# Register your models here.


@admin.register(NoteTag)
class NoteTagAdmin(admin.ModelAdmin):
	list_display = ('name', 'owner', 'created', 'updated', 'priority', 'attr1', 'attr2')
	search_fields = ('name', 'owner')
	list_filter = ('owner', 'created', 'updated', 'attr1', 'attr2')
	date_heirarchy = 'updated'


@admin.register(PageTag)
class PageTagAdmin(admin.ModelAdmin):
	list_display = ('name', 'owner', 'created', 'updated', 'priority', 'attr1', 'attr2')
	search_fields = ('name', 'owner')
	list_filter = ('owner', 'created', 'updated', 'attr1', 'attr2')
	date_heirarchy = 'updated'


@admin.register(EventTag)
class EventTagAdmin(admin.ModelAdmin):
	list_display = ('name', 'owner', 'created', 'updated', 'priority', 'attr1', 'attr2')
	search_fields = ('name', 'owner')
	list_filter = ('owner', 'created', 'updated', 'attr1', 'attr2')
	date_heirarchy = 'updated'


@admin.register(DayTag)
class DayTagAdmin(admin.ModelAdmin):
	list_display = ('name', 'owner', 'created', 'updated', 'priority', 'attr1', 'attr2')
	search_fields = ('name', 'owner')
	list_filter = ('owner', 'created', 'updated', 'attr1', 'attr2')
	date_heirarchy = 'updated'
