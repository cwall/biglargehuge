from blh.gameify.models import Season, Gameify
from django.views.generic import DetailView
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404

def gameify(request):
	gameifycast = Gameify.objects.all().order_by('-date').filter(publish=True)
	recent = Gameify.objects.latest()
	return render_to_response('gameify/gameify-list.html', {'gameifycast': gameifycast, 'recent':recent}, context_instance=RequestContext(request))

def gameify_details(request, gameifyslug):
	gameify = get_object_or_404(Gameify, slug=gameifyslug)
	return render_to_response('gameify/gameify-detail.html', {'gameify': gameify}, context_instance=RequestContext(request))