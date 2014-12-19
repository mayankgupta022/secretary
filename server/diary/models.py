from django.db import models
# Create your models here.


class Calender(models.Model):
	owner = models.CharField(max_length = 300)
	name = models.CharField(max_length = 300)
	created = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
	priority = models.IntegerField(max_length = 10, default = 0)
	active = models.IntegerField(max_length = 1, default = 0)#0 = yes, 1 = no
	attr1 = models.CharField(max_length = 300, blank = True)
	attr2 = models.CharField(max_length = 300, blank = True)
	def __unicode__(self):
		return self.name


class Event(models.Model):
	name = models.CharField(max_length = 300)
	calender = models.ForeignKey(Calender, on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
	start = models.DateTimeField()
	end = models.DateTimeField()
	remind = models.IntegerField(max_length = 1, default = 0)#0 = no, 1 = yes
	reminder = models.DateTimeField(blank = True)
	priority = models.IntegerField(max_length = 10, default = 0)
	active = models.IntegerField(max_length = 1, default = 0)#0 = active, 1 = trash
	attr1 = models.CharField(max_length = 300, blank = True)
	attr2 = models.CharField(max_length = 300, blank = True)
	desc = models.TextField(blank = True)
	def __unicode__(self):
		return self.name


class Day(models.Model):
	owner = models.CharField(max_length = 300)
	date = models.DateField(unique = True)
	created = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
	content = models.TextField(blank = True)
	attr1 = models.CharField(max_length = 300, blank = True)
	attr2 = models.CharField(max_length = 300, blank = True)
	def __unicode__(self):
		return str(self.date)
