from __future__ import absolute_import, print_function, unicode_literals
# from django.conf import settings
# from django.conf.urls import patterns, include, url

from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
# from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve


# from django.contrib import admin
from django.views.generic import ListView, DetailView
from blh.thebroadcast.views import *
from blh.thebroadcast.models import *
from blh.games.models import Platform, Games, Verdict, Review
from blh.games.views import games_list, game_details, review_list, review_detail
from blh.blindbuy.models import *
from blh.blindbuy.views import bb_details
from blh.home.views import home
from blh.gameify.views import gameify, gameify_details
from blh.gameify.models import Gameify, Season
from blh.greatmoments.models import Gmig
from blh.greatmoments.views import GreatMomentsList, gmig_details
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from blh.thebroadcast.feeds import BroadcastFeed
from blh.sitemap.models import CastSitemap, BlindbuySitemap, GamesSitemap, GmigSitemap
admin.autodiscover()

#	System URLS
urlpatterns = [
    # url(r'^sitemap\.xml$', sitemap,
        # {'sitemaps': {'cmspages': CMSSitemap}}),
]

urlpatterns += i18n_patterns(
    url(r'^admin/', include(admin.site.urls)),  # NOQA
    url(r'^', include('cms.urls')),
)

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns = [
        url(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        ] + staticfiles_urlpatterns() + urlpatterns


urlpatterns = ('',
		# url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),
    # url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps})
)
# urlpatterns += ('',
#     url(r'uploader/', include('chunked_uploads.urls')),
# )

#	Home url
urlpatterns += ('blh.home.views',
	url(r'^$', include('blh.home')),
	# url(r'^accounts/', include('allauth.urls')),
)



#	Broadcast URL
urlpatterns += i18n_patterns(
# urlpatterns += patterns('blh.thebroadcast.views',
    url(r'^the-broadcast/$', 'cast', name='broadcast-list'),
    url(r'^the-broadcast/(?P<castslug>.*)/$', 'cast_details', name='broadcast-details'),
)

urlpatterns += patterns('',
    url(r'^rss/the-broadcast/$', BroadcastFeed()),
)

#	Games URL's
urlpatterns += patterns('blh.games.views',
	url(r'^games/$', 'games_list', name='games-list'),
	
	url(r'^games/(?P<gameslug>.*)/$', 'game_details', name='game-details'),

	url(r'^reviews/$', 'review_list', name='review-list'),
	url(r'^reviews/(?P<reviewslug>.*)/$', 'review_detail', name='review')
)

#	Blind Buy URL
urlpatterns += patterns('blh.blindbuy.views',
	url(r'^blind-buy/$', ListView.as_view(
		model = Blindbuy,
		queryset = Blindbuy.objects.all().order_by('date'),
		template_name = 'blindbuy/blindbuy-list.html'
	)),
	
 	url(r'^blind-buy/(?P<bbslug>.*)/$', 'bb_details', name='bb' ),

)

#	Gameify
urlpatterns += patterns('blh.gameify.views',
	url(r'^gameify/$', 'gameify', name='gameify'),
	url(r'^gameify/(?P<gameifyslug>.*)/$', 'gameify_details', name='game' ),
)

#	GMIG URL
urlpatterns += patterns('blh.greatmoments.views',
	url(r'^great-moments-in-gaming/$', GreatMomentsList.as_view()),
 	url(r'^great-moments-in-gaming/(?P<gmigslug>.*)/$', 'gmig_details', name='gmig' ),

)

#	Include URL
urlpatterns += patterns('',
	#url(r'^', include('blh.contact.urls')),
 	url(r'^', include('blh.features.urls')),
)

#	Media URL
# if settings.DEBUG:
# 	urlpatterns += patterns('',
# 		url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
# 	)

# urlpatterns += staticfiles_urlpatterns()
	