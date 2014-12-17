from django.contrib import admin
from pages.models import *
# Register your models here.


class NotebookAdmin(admin.ModelAdmin):
	list_display = ('owner', 'name', 'created', 'updated', 'priority', 'attr1', 'attr2')
	search_fields = ('owner', 'name', 'created', 'updated', 'priority', 'attr1', 'attr2')
	list_filter = ('owner', 'name', 'created', 'updated', 'priority', 'attr1', 'attr2')
	date_heirarchy = ('created', 'updated')
#	filter_horizontal = ('attr1', 'attr2')


class PageAdmin(admin.ModelAdmin):
	list_display = ('owner', 'name', 'notebook', 'created', 'updated', 'context', 'active', 'priority', 'attr1', 'attr2')
	search_fields = ('owner', 'name', 'notebook', 'created', 'updated', 'context', 'active', 'priority', 'attr1', 'attr2')
	list_filter = ('owner', 'name', 'notebook', 'created', 'updated', 'context', 'active', 'priority', 'attr1', 'attr2')
	date_heirarchy = ('created', 'updated')
#	filter_horizontal = ('context', 'active', 'attr1', 'attr2')


admin.site.register(Notebook,NotebookAdmin)
admin.site.register(Page,PageAdmin)