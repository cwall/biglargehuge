from blh.features.models import Category, Content, Topic, Feature, Rating
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
 
def category_page(request, categorySlug):
	category = get_object_or_404(Category, slug=categorySlug)
	return render_to_response('features/category.html',{'category': category}, context_instance=RequestContext(request))

def feature_list(request):
  features = Feature.objects.all().filter(publish=True)
  paginator = Paginator(features, 15)
  page = request.GET.get('page')
  try:
    features = paginator.page(page)
  except PageNotAnInteger:
    features = paginator.page(1)
  except EmptyPage:
    features = paginator.page(paginator.num_pages)
  
  return render_to_response('features/features-list.html', {'features':features}, context_instance=RequestContext(request))

def feature_detail(request, catslug, featureslug):
	feature = get_object_or_404(Feature, category__slug=catslug, slug=featureslug)   	
	return render_to_response('features/features-detail.html', {'feature': feature}, context_instance=RequestContext(request))