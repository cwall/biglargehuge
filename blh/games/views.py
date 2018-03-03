from blh.games.models import Games, Verdict, Review
from django.views.generic import DetailView
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404

def games_list(request):
	games = Games.objects.all().filter(publish=True)
	return render_to_response('games/games-list.html', {'games':games}, context_instance=RequestContext(request))
	
def game_details(request, gameslug):
	game = get_object_or_404(Games, slug=gameslug)
	return render_to_response('games/games-detail.html', {'game':game}, context_instance=RequestContext(request))

def review_list(request):
	reviews = Review.objects.all().filter(publish=True).order_by('-date')
	return render_to_response('games/games-reviews.html', {'reviews':reviews}, context_instance=RequestContext(request))

def review_detail(request, reviewslug):
	review = get_object_or_404(Review, slug=reviewslug)
	return render_to_response('games/games-review-details.html', {'review':review}, context_instance=RequestContext(request))