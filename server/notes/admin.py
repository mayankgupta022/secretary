from django.contrib import admin
from notes.models import *
# Register your models here.

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
	list_display = ('name', 'owner', 'created', 'updated', 'context', 'active', 'priority', 'attr1', 'attr2')
	search_fields = ('name', 'owner')
	list_filter = ('owner', 'created', 'updated', 'context', 'active', 'priority', 'attr1', 'attr2')
	date_heirarchy = 'updated'