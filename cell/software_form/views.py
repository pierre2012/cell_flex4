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


from django.conf import settings
from django.core.mail import send_mail
from django.views.generic import FormView

from forms import SubmissionForm

from models import Submission

class ContactFormView(FormView):

    form_class = SubmissionForm
    template_name = "software_form/email_form.html"
    success_url = '/download/thankyou/'

    def form_valid(self, form):
        # header = "{email} supplied a form!".format(
        #     email=form.cleaned_data.get('email_address'))
        # message = "\n\nType: {0}".format(form.cleaned_data.get('ticket_type').encode('utf-8'))
        # message += "\n\nCourt: {0}".format(form.cleaned_data.get('group_court'))
        # message += "\n\ncontact_method: {0}".format(form.cleaned_data.get('contact_method'))
        # send_mail(
        #     subject=header,
        #     message=message,
        #     from_email='contact@trafficcounsel.com',
        #     recipient_list=['dkoonce@gmail.com'],
        # )
        
        c = Submission()

        c.software_download = form.cleaned_data.get('software_download')
        c.email_address = form.cleaned_data.get('email_address')
        c.submitter_name = form.cleaned_data.get('submitter_name')
        c.institution = form.cleaned_data.get('institution')
        
        c.save()
        
        return super(ContactFormView, self).form_valid(form)
        
        
def thankyou(request):
	return render_to_response('software_form/thankyou.html')