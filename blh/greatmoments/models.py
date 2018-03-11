from django.db import models
from blh.games.models import Games
from datetime import datetime
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class Gmig(models.Model):
	game = models.ForeignKey(Games, blank=True)
	title = models.CharField(max_length=250)
	slug = models.SlugField(unique=True)
	date = models.DateField()
	author = models.ForeignKey(User)
	cover = models.ImageField(upload_to='./gmig/banners/', blank=True)
	video = models.CharField(max_length=600, blank=True,)
	content = models.CharField(max_length=500)
	publish = models.BooleanField()
	
	class Meta:
		ordering = ['title']
		verbose_name_plural = 'Great Moments in Gaming'
		get_latest_by = 'date'

	def __unicode__(self):
		return u'%s %s' % (self.game.title, self.title)

	def get_absolute_url(self):
		return reverse('blh.greatmoments.views.gmig_details', args=[str(self.slug)])