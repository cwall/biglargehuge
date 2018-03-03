from blh.thebroadcast.models import Broadcast
from blh.about.models import Staff
from django.views.generic import DetailView
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def cast(request):
  broadcast = Broadcast.objects.all().order_by('-date').filter(publish=True)
  paginator = Paginator(broadcast,9)
  page = request.GET.get('page')
  try:
    broadcast = paginator.page(page)
  except PageNotAnInteger:
    broadcast = paginator.page(1)
  except EmptyPage:
    broadcast = paginator.page(paginator.num_pages)

  return render_to_response('thebroadcast/broadcast-list.html', {'broadcast': broadcast}, context_instance=RequestContext(request))
  
def cast_details(request, castslug):
	cast = get_object_or_404(Broadcast, slug=castslug)
	staff = Staff.objects.all()
	return render_to_response('thebroadcast/broadcast-detail.html', {'cast': cast, 'staff': staff}, context_instance=RequestContext(request))