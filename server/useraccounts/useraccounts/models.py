from django.db import models
# Create your models here.


class Calender(models.Model):
	owner = models.CharField(max_length = 300)
	name = models.CharField(max_length = 300)
	created = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
	priority = models.IntegerField(max_length = 10, default = 0)
	display = models.IntegerField(max_length = 1, default = 0)#0 = yes, 1 = no
	attr1 = models.CharField(max_length = 300, blank = True)
	attr2 = models.CharField(max_length = 300, blank = True)
	def __unicode__(self):
		return self.name


class Event(models.Model):
	name = models.CharField(max_length = 300)
	calender = ForeignKey(Calender)
	created = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
	start = models.DateTimeField()
	end = models.DateTimeField()
	reminder = models.DateTimeField(blank = True)
	desc = models.TextField(blank = True)
	priority = models.IntegerField(max_length = 10, default = 0)
	attr1 = models.CharField(max_length = 300, blank = True)
	attr2 = models.CharField(max_length = 300, blank = True)
	def __unicode__(self):
		return self.name


class Day(models.Model):
	owner = models.CharField(max_length = 300)
	date = models.DateTimeField(unique = True)
	created = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
	content = models.TextField(blank = True)
	attr1 = models.CharField(max_length = 300, blank = True)
	attr2 = models.CharField(max_length = 300, blank = True)
	def __unicode__(self):
		return self.name
