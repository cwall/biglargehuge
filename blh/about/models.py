from django.db import models

class Staff(models.Model):
	name = models.CharField(max_length=200)
	title = models.CharField(max_length=200, blank=True)
	bio = models.CharField(max_length=255, blank=True)
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
	body = models.CharField(max_length=500)
	
	def __unicode__(self):
		return self.title
