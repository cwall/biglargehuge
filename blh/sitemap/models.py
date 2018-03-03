from django.db import models
from django.contrib.sitemaps import Sitemap
from blh.thebroadcast.models import *
from blh.features.models import Content
from blh.gameify.models import *
from blh.games.models import *
from blh.greatmoments.models import *
from blh.blindbuy.models import *

class CastSitemap(Sitemap):
    changefreq = "never"
    priority = 0.6

    def items(self):
        return Broadcast.objects.filter(publish=True)

    def lastmod(self, obj):
        return obj.date

# class FeatureSitemap(Sitemap):
#     changefreq = "never"
#     priority = 0.6
# 
#     def items(self):
#         return Content.objects.filter(publish=True)
# 
#     def lastmod(self, obj):
#         return obj.date

class GameifySitemap(Sitemap):
    changefreq = "never"
    priority = 0.6

    def items(self):
        return gameify.objects.filter(publish=True)

    def lastmod(self, obj):
        return obj.date

class GamesSitemap(Sitemap):
    changefreq = "never"
    priority = 0.6

    def items(self):
        return Games.objects.filter(publish=True)

class BlindbuySitemap(Sitemap):
    changefreq = "never"
    priority = 0.6

    def items(self):
        return Blindbuy.objects.filter(publish=True)

    def lastmod(self, obj):
        return obj.date

class GmigSitemap(Sitemap):
    changefreq = "never"
    priority = 0.6

    def items(self):
        return Gmig.objects.filter(publish=True)

    def lastmod(self, obj):
        return obj.date