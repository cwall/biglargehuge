from django.conf.urls import patterns, include, url
from blh.features.views import feature_list

urlpatterns = patterns('blh.features.views',
  url(r'^features/$', 'feature_list', name='feature-list'),  
  #url(r'^(?P<catslug>[-\w]+)/(?P<featureslug>[-\w]+)/$', 'feature_detail', name='feature-detail'),
  #url(r'^(?P<categorySlug>[-\w]+)/$', 'category_page', name='category-page'),
)