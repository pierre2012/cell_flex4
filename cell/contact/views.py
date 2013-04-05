from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.http import Http404
from django.core.urlresolvers import reverse
from django.conf.urls.defaults import *

from django.core import serializers

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core import serializers

from datetime import datetime
from random import randint

from django.views.decorators.csrf import csrf_exempt


from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext, Context
from django.core.mail import send_mail, BadHeaderError


from models import ContactForm


@csrf_exempt
def contact(request):
	if request.method == 'POST': # If the form has been submitted...
		form = ContactForm(request.POST) # A form bound to the POST data
		if form.is_valid(): # All validation rules pass
			subject = form.cleaned_data['subject']
			message = form.cleaned_data['message']
			sender = form.cleaned_data['sender']

			form.save()
			return HttpResponseRedirect('/contact/thankyou/') # Redirect after POST
	else:
		form = ContactForm() # An unbound form

	return render_to_response('contact/contact.html', {'form': form, })
    
def thankyou(request):
	return render_to_response('contact/thankyou.html')
