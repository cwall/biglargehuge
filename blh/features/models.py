from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.contenttypes.fields import GenericForeignKey

class Topic(models.Model):
	title = models.CharField(max_length=250)
	overview = models.CharField(max_length=500, blank=True)
	cover = models.ImageField(upload_to='./topics/', blank=True)
	date = models.DateField()
	updated = models.DateTimeField(auto_now=True)
	slug = models.SlugField(unique=True)
	extra_info = models.CharField(max_length=500, blank=True)
	
	class Meta:
		ordering = ['-updated']
		
	def __unicode__(self):
		return self.title
	
class Category(models.Model):
	title = models.CharField(max_length=250)
	slug = models.SlugField(unique=True)
	itself = models.ForeignKey('self', blank=True, null=True, related_name='parent')
	
	class Meta:
		ordering = ['title']
		verbose_name_plural = 'Categories'
	
	def __unicode__(self):
		return self.title


class Rating(models.Model):
	rating = models.CharField(max_length=50)
	slug = models.SlugField(unique=True)
	
	class Meta:
		ordering = ['rating']
  
	def __unicode__(self):
		return self.rating
			
class Feature(models.Model):	
	#Main fields
	author = models.ForeignKey(User)
	category = models.ForeignKey(Category)
	title = models.CharField(max_length=250)
	subhead = models.CharField(max_length=250, blank=True)
	body = models.CharField(max_length=500, )	
	date = models.DateField()
	date_updated = models.DateTimeField(auto_now=True)
	cover = models.ImageField(upload_to='./features/%Y/%m/%d/', blank=True)
		
	#Audio/Podcast fields
	audio_file = models.FileField(blank=True)
	audio_description = models.CharField(max_length=500, blank=True)
	attachment = models.FileField(blank=True)
	
	#Review field
	verdict = models.TextField(blank=True)
	rating = models.ForeignKey(Rating, blank=True, null=True, help_text='Buy, Skip & Rent are for Games. Star ratings are for features')
	
	#Meta fields
	excerpt = models.TextField(blank=True)
	feature_class = models.SlugField(blank=True)	
	meta_keywords = models.CharField(max_length=300, blank=True, help_text='Separate your keywords with commas.')
	
	#Conetnt feature fields
	related_content = models.ManyToManyField('self', blank=True)
	topics = models.ManyToManyField('Topic', blank=True)
	url = models.URLField(blank=True)
	
	#Sorting fields
	featured = models.BooleanField()
	publish = models.BooleanField()
	slug = models.SlugField(unique=True)
	
	class Meta:
		ordering = ['category', 'date', 'publish']
		verbose_name_plural = "Featured Entries"
		get_latest_by = "date"
		
	def __unicode__(self):
		return self.title
		
	def is_published(self):
		return self.publish
	
	def get_absolute_url(self):
		return reverse('blh.features.views.feature_detail', args=[self.category.slug,self.slug])
	
# 	def get_absolute_url(self):
# 		return reverse('blh.features.views.feature_detail', '/%s/%s/' % (str(self.category.slug), self.slug))
	

class Content(models.Model):
	header = models.CharField(max_length=200, blank=True)
	body = models.CharField(max_length=500, blank=True)
	image = models.ImageField(upload_to='./features/%Y/%m/%d/', blank=True)
	content_class = models.SlugField(unique=True, blank=True, null=True)
	feature = models.ForeignKey(Feature)
		
	class Meta:
		ordering = ['header']
		verbose_name_plural = 'Block Content'
		
	def __unicode__(self):
		return self.header