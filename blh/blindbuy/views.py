from blh.blindbuy.models import Blindbuy
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404

def bb_details(request, bbslug):
	bb = get_object_or_404(Blindbuy, slug=bbslug)
	return render_to_response('blindbuy/blindbuy-detail.html', {'bb': bb}, context_instance=RequestContext(request))
