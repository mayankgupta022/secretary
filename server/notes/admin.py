from django.contrib import admin
from notes.models import *
# Register your models here.


class NoteAdmin(admin.ModelAdmin):
	list_display = ('owner', 'name', 'created', 'updated', 'context', 'active', 'priority', 'attr1', 'attr2')
	search_fields = ('owner', 'name', 'created', 'updated', 'context', 'active', 'priority', 'attr1', 'attr2')
	list_filter = ('owner', 'name', 'created', 'updated', 'context', 'active', 'priority', 'attr1', 'attr2')
	date_heirarchy = ('created', 'updated')
#	filter_horizontal = ('context', 'active', 'attr1', 'attr2')


admin.site.register(Note,NoteAdmin)