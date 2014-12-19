from django.contrib import admin
from pages.models import *
# Register your models here.


@admin.register(Notebook)
class NotebookAdmin(admin.ModelAdmin):
	list_display = ('name', 'owner', 'stack', 'created', 'updated', 'priority', 'attr1', 'attr2')
	search_fields = ('name', 'owner', 'stack')
	list_filter = ('owner', 'created', 'updated', 'attr1', 'attr2')
	date_heirarchy = 'updated'


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
	list_display = ('name', 'owner', 'notebook', 'created', 'updated', 'context', 'active', 'priority', 'attr1', 'attr2')
	search_fields = ('name', 'owner', 'notebook')
	list_filter = ('owner', 'created', 'updated', 'context', 'active', 'attr1', 'attr2')
	date_heirarchy = 'updated'


@admin.register(Stack)
class StackAdmin(admin.ModelAdmin):
	list_display = ('name', 'owner', 'created', 'updated', 'priority', 'attr1', 'attr2')
	search_fields = ('name', 'owner')
	list_filter = ('owner', 'created', 'updated', 'priority', 'attr1', 'attr2')
	date_heirarchy = 'updated'
