from django.contrib import admin
from pages.models import *
# Register your models here.


class NotebookAdmin(admin.ModelAdmin):
	list_display = ('owner', 'name', 'stack', 'created', 'updated', 'priority', 'attr1', 'attr2')
	search_fields = ('owner', 'name', 'stack', 'created', 'updated', 'priority', 'attr1', 'attr2')
	list_filter = ('owner', 'name', 'stack', 'created', 'updated', 'priority', 'attr1', 'attr2')
	date_heirarchy = ('created', 'updated')


class PageAdmin(admin.ModelAdmin):
	list_display = ('owner', 'name', 'notebook', 'created', 'updated', 'context', 'active', 'priority', 'attr1', 'attr2')
	search_fields = ('owner', 'name', 'notebook', 'created', 'updated', 'context', 'active', 'priority', 'attr1', 'attr2')
	list_filter = ('owner', 'name', 'notebook', 'created', 'updated', 'context', 'active', 'priority', 'attr1', 'attr2')
	date_heirarchy = ('created', 'updated')


class StackAdmin(admin.ModelAdmin):
	list_display = ('owner', 'name', 'created', 'updated', 'priority', 'attr1', 'attr2')
	search_fields = ('owner', 'name', 'created', 'updated', 'priority', 'attr1', 'attr2')
	list_filter = ('owner', 'name', 'created', 'updated', 'priority', 'attr1', 'attr2')
	date_heirarchy = ('created', 'updated')


admin.site.register(Notebook,NotebookAdmin)
admin.site.register(Page,PageAdmin)
admin.site.register(Stack,StackAdmin)
