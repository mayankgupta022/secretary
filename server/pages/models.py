from django.db import models
from django.core.files.storage import FileSystemStorage
# Create your models here.


class Stack(models.Model):
	owner = models.CharField(max_length = 300)
	name = models.CharField(max_length = 300)
	created = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
	priority = models.IntegerField(max_length = 10, default = 0)
	attr1 = models.CharField(max_length = 300, blank = True)
	attr2 = models.CharField(max_length = 300, blank = True)
	def __unicode__(self):
		return self.name


class Notebook(models.Model):
	owner = models.CharField(max_length = 300)
	name = models.CharField(max_length = 300)
	stack = models.IntegerField(max_length = 10, default = 0)
	created = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
	priority = models.IntegerField(max_length = 10, default = 0)
	attr1 = models.CharField(max_length = 300, blank = True)
	attr2 = models.CharField(max_length = 300, blank = True)
	def __unicode__(self):
		return self.name


class Page(models.Model):
	owner = models.CharField(max_length = 300)
	name = models.CharField(max_length = 300)
	notebook = models.ForeignKey(Notebook)
	created = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
	context = models.IntegerField(max_length = 2, default = 1)#0 = text page, 1 = image page...
	active = models.IntegerField(max_length = 1, default = 0)#0 = active, 1 = trash
	priority = models.IntegerField(max_length = 10, default = 0)
	attr1 = models.CharField(max_length = 300, blank = True)
	attr2 = models.CharField(max_length = 300, blank = True)
	content = models.TextField(blank = True)
	def __unicode__(self):
		return self.name