from django.contrib.syndication.views import Feed
from blh.thebroadcast.models import Broadcast
from django.utils import feedgenerator
from datetime import datetime, time

class BroadcastFeed(Feed):
	
	feed_type = feedgenerator.Rss201rev2Feed
	title = "The Broadcast Feed"
	link = "/the-broadcast/"
	description = "Join the Big Large Huge crew as they discuss video games each week on The BroadCast!"
		
	def author_name(self):
		author_name = "Big Large Huge"
	
	def author_email(self):
		author_email = "info@biglargehuge.com"
			
	def feed_url(self):
		feed_url = "/rss/the-broadcast/"
		
	def items(self):
		return Broadcast.objects.all().order_by('-date')[:5]

	def item_pubdate(self, item):
		return datetime.combine(item.date, time())
			
	def item_title(self, item):
		return item.title

	def item_link(self, item):
		return item.get_absolute_url()
	
	def item_description(self, item):
		return item.excerpt
        	
	def item_enclosure_url(self, item):
		return item.podcast.url
	
	def item_enclosure_length(self, item):
		return item.podcast
 		
	item_enclosure_mime_type = "audio/mpeg"
	
