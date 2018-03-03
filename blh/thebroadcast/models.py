from django.db import models
from datetime import datetime
from blh.games.models import Games
from blh.about.models import Staff
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.core.urlresolvers import reverse
from chunked_uploads.fields import ChunkedFileField

class Broadcast(models.Model):
	author = models.ForeignKey(User)
	title = models.CharField(max_length=250)
	slug = models.SlugField(unique=True)
	episode = models.PositiveIntegerField()
	date = models.DateField()
	podcast = ChunkedFileField(blank=True)
  	crew = models.ManyToManyField(Staff)
	content = HTMLField()
	excerpt = models.TextField(blank=True)
	gaming = models.ManyToManyField(Games, blank=True)
	cover = models.ImageField(upload_to='./the-broadcast/featured-img/%Y/%m/%d/', blank=True)
	publish = models.BooleanField()
	
	def __unicode__(self):
		return self.title
	
	class Meta:
		verbose_name_plural = 'The BroadCast'
		get_latest_by = "date"
	
	def get_absolute_url(self):
		return reverse('blh.thebroadcast.views.cast_details', args=[str(self.slug)])
