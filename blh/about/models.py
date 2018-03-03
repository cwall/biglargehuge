from django.db import models
from tinymce.models import HTMLField

class Staff(models.Model):
	name = models.CharField(max_length=200)
	title = models.CharField(max_length=200, blank=True)
	bio = HTMLField(blank=True)
	avatar = models.ImageField(upload_to='./staff/', blank=True)
	url = models.URLField(blank=True)
	twitter = models.CharField(max_length=250, blank=True)
	email = models.EmailField(blank=True)
	slug = models.SlugField(unique=True)
	
	class Meta:
		ordering = ['name']
		verbose_name_plural = 'The Staff'
		
	def __unicode__(self):
		return self.name
	

class About(models.Model):
	title = models.CharField(max_length=255)
	body = HTMLField()
	
	def __unicode__(self):
		return self.title
