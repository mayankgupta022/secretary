from django.db import models
from diary.models import Event, Day
from pages.models import Page
from notes.models import Note
# Create your models here.


class NoteTag(models.Model):
	owner = models.CharField(max_length = 300)
	name = models.CharField(max_length = 300)
	created = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
	priority = models.IntegerField(max_length = 10, default = 0)
	attr1 = models.CharField(max_length = 300, blank = True)
	attr2 = models.CharField(max_length = 300, blank = True)
	entities = models.ManyToManyField(Note, related_name = "tags")
	def __unicode__(self):
		return self.name


class PageTag(models.Model):
	owner = models.CharField(max_length = 300)
	name = models.CharField(max_length = 300)
	created = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
	priority = models.IntegerField(max_length = 10, default = 0)
	attr1 = models.CharField(max_length = 300, blank = True)
	attr2 = models.CharField(max_length = 300, blank = True)
	entities = models.ManyToManyField(Page, related_name = "tags")
	def __unicode__(self):
		return self.name


class EventTag(models.Model):
	owner = models.CharField(max_length = 300)
	name = models.CharField(max_length = 300)
	created = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
	priority = models.IntegerField(max_length = 10, default = 0)
	attr1 = models.CharField(max_length = 300, blank = True)
	attr2 = models.CharField(max_length = 300, blank = True)
	entities = models.ManyToManyField(Event, related_name = "tags")
	def __unicode__(self):
		return self.name


class DayTag(models.Model):
	owner = models.CharField(max_length = 300)
	name = models.CharField(max_length = 300)
	created = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
	priority = models.IntegerField(max_length = 10, default = 0)
	attr1 = models.CharField(max_length = 300, blank = True)
	attr2 = models.CharField(max_length = 300, blank = True)
	entities = models.ManyToManyField(Day, related_name = "tags")
	def __unicode__(self):
		return self.name
