from django.db import models
from datetime import datetime
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class Platform(models.Model):
	title = models.CharField(max_length=250)
	slug = models.SlugField(unique=True)
	cover = models.ImageField(upload_to='./platform/consoles/', blank=True)
		
	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ['title']
						
class Games(models.Model):
	title = models.CharField(max_length=250)
	slug = models.SlugField(unique=True)
	cover = models.ImageField(upload_to='./games/covers/', blank=True)
	platform = models.ManyToManyField(Platform)
	content = HTMLField(blank=True)
	publish = models.BooleanField()
	
	class Meta:
		ordering = ['title']
		verbose_name_plural = 'Video Games'
	
	def __unicode__(self):
		return self.title
	
	def admin_img(self):
		return '<img src="/media/%s" />' % self.cover
	admin_img.allow_tags = True

	def get_absolute_url(self):
		return reverse('blh.games.views.game_details', args=[str(self.slug)])
		
class Verdict(models.Model):
	verdict = models.CharField(max_length=60)
	slug = models.SlugField()
	
	class Meta:
		ordering = ['verdict']
	
	def __unicode__(self):
		return self.verdict
		
class Review(models.Model):
	game = models.ForeignKey(Games)
	title = models.CharField(max_length=200)
	subtitle = models.CharField(max_length=200, help_text='Text that hints at the quality of the game')
	slug = models.SlugField(unique=True)
	author = models.ForeignKey(User)
	date = models.DateTimeField(auto_now=True)
	content = HTMLField(blank=True)
	breakdown = models.CharField(max_length=250, help_text='Your final thoughts on the game')
	verdict = models.ForeignKey(Verdict, blank=True)
	publish = models.BooleanField()
	
	class Meta:
		ordering = ['-date']
		get_latest_by = 'date'
	
	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blh.games.views.review_detail', args=[str(self.slug)])