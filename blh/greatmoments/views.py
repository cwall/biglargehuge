from blh.greatmoments.models import Gmig
from django.views.generic import ListView, DetailView
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class GreatMomentsList(ListView):
	template_name = 'gmig/gmig-list.html'
	context_object_name = 'gmig_list'
	queryset = Gmig.objects.all().order_by('-date').filter(publish=True)
	

def gmig_details(request, gmigslug):
	gmig = get_object_or_404(Gmig, slug=gmigslug)
	othermoments = Gmig.objects.all().filter(publish=True)
	return render_to_response('gmig/gmig-detail.html', {'gmig': gmig, 'othermoments': othermoments}, context_instance=RequestContext(request))

#def pagination(request):
#	gmig_listing = Gmig.objects.all()
#	paginator = Paginator(gmig_listing, 10)
#	
#	page = request.GET.get('page')
#	try:
#		gmig = paginator.page(page)
#	except PageNotAnInteger:
#		gmig = paginator.page(1)
#	except EmptyPage:
#		gmig = paginator.page(paginator.num_pages)
#	return render_to_response('gmig/gmig-list', {'gmig-pagination':gmig-pagination})