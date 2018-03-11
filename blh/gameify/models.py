from django.db import models
from datetime import datetime
from blh.guests.models import Guest
from django.contrib.auth.models import User
# from tinymce.models import models.HTMLField
from django.core.urlresolvers import reverse

class Season(models.Model):
	season = models.CharField(max_length=60)
	slug = models.SlugField(unique=True)
	
	def __unicode__(self):
		return self.season
	
class Gameify(models.Model):
	season = models.ForeignKey(Season)
	episode = models.PositiveIntegerField()
	author = models.ForeignKey(User)
	date = models.DateField()
	podcast = models.FileField(blank=True)
	title = models.CharField(max_length=250, unique=True)
	subtitle = models.CharField(max_length=200, blank=True, help_text='Add the overall topic here ex: Hallucinations')
	cover = models.ImageField(upload_to='./gameify/featured-images/%Y/%m/%d/', blank=True)
	content = models.CharField(help_text='Describe the podcast', blank=True)
	breakdown = models.CharField(blank=True, help_text='Describe the game you create aka We GAMEify: ***')
	gameify_doc = models.FileField(upload_to='./gameify/pdfs/%Y/%m/%d/', blank=True)
	guest = models.ForeignKey(Guest, blank=True, null=True)
	slug = models.SlugField(unique=True, help_text='This will auto-populate and serve as the base for the url.')
	publish = models.BooleanField()
	
	class Meta:
		verbose_name_plural = 'GAMEify'
		ordering = ['title']
		get_latest_by = 'date'
		
	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blh.gameify.views.gameify_details', args=[str(self.slug)])