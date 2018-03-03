from django.db import models
from tinymce.models import HTMLField

class Guest(models.Model):
	name = models.CharField(max_length=250)
	image = models.ImageField(upload_to='./guests/photos/', blank=True)
	company = models.CharField(max_length=250, blank=True)
	url = models.URLField(blank=True)
	bio = HTMLField(blank=True)
	indie_dev = models.BooleanField()
	
	class Meta:
		ordering = ['name']
	
	def __unicode__(self):
		return self.name