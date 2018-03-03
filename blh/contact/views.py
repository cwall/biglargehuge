from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from blh.contact.forms import ContactForm
from django.template import RequestContext
from django.core.mail import send_mail

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)

		if form.is_valid():
			subject = form.cleaned_data['subject']
			email = form.cleaned_data['email']
			message = form.cleaned_data['message']
			send_mail(subject, message, email, ['blh@biglargehuge.com'], fail_silently=False)
			return HttpResponseRedirect('/thanks/')
	else:
		form = ContactForm()
	return render_to_response('contact/contact.html', {'form': form}, context_instance=RequestContext(request))

def thanks(request):
	return render_to_response('contact/thanks.html', context_instance=RequestContext(request))
