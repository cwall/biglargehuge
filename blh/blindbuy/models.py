from django.db import models
from datetime import datetime
from blh.games.models import Games
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.core.urlresolvers import reverse

class Blindbuy(models.Model):
	author = models.ForeignKey(User)
	title = models.CharField(max_length=250)
	slug = models.SlugField(unique=True)
	date = models.DateField()
	episode = models.PositiveIntegerField()
	video = models.CharField(max_length=500)
	game = models.ForeignKey(Games, related_name='blindbuys', blank=True)
	content = HTMLField(blank=True)
	publish = models.BooleanField()
	
	class Meta:
		ordering = ['date', 'title']
		verbose_name = 'Blind Buy'
		verbose_name_plural = 'Blind Buys'
		get_latest_by = 'date'
	
	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blh.blindbuy.views.bb_details', args=[str(self.slug)])