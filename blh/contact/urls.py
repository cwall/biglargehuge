from django.conf.urls import patterns, include, url
from blh.contact.views import contact

urlpatterns = patterns('blh.contact.views',
	url(r'^contact/$', 'contact', name='contact'),
	url(r'^thanks/$', 'thanks', name='thanks'),
)