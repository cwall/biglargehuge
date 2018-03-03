from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from blh.thebroadcast.models import Broadcast
from blh.blindbuy.models import Blindbuy
from blh.gameify.models import Gameify
from blh.games.models import Games, Review
from blh.greatmoments.models import Gmig
#from blh.features.models import Content

def home(request):
	bclist = Broadcast.objects.all().order_by('-date').filter(publish=True)[:7]
	blindbuy = Blindbuy.objects.latest()
	games = Games.objects.all().filter(publish=True)[:10]
	reviews = Review.objects.all().order_by('-date').filter(publish=True)[:3]
	gmig = Gmig.objects.all().order_by('-date').filter(publish=True)[:3]
	gameify = Gameify.objects.all()
# 	feat = Content.objects.all().order_by('-date').filter(publish=True)[0]
# 	feature = Content.objects.all().order_by('-date').filter(publish=True)[1:4]
	return render_to_response('home/home.html', {'bclist': bclist, 'blindbuy': blindbuy, 'games': games, 'gmig':gmig, 'gameify':gameify,  'reviews':reviews}, context_instance=RequestContext(request))
	
