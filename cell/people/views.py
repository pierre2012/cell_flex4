from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.http import Http404
from django.core.urlresolvers import reverse
from django.conf.urls.defaults import *


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core import serializers


from models import Person

def people(request):
	
	faculty_data = Person.objects.filter(member_type=0).order_by('sortorder')
	postdoc_data = Person.objects.filter(member_type=1).order_by('sortorder')
	grad_data = Person.objects.filter(member_type=2).order_by('sortorder')
	under_data = Person.objects.filter(member_type=3).order_by('sortorder')
	collab_data = Person.objects.filter(member_type=4).order_by('sortorder')
	alumni_data = Person.objects.filter(member_type=5).order_by('sortorder')
		
	return render_to_response('people/list.html', {'faculty_data': faculty_data,'postdoc_data': postdoc_data,
                'grad_data': grad_data,'under_data': under_data,'collab_data': collab_data,
                'alumni_data': alumni_data }, context_instance=RequestContext(request))


def person_detail(request, person):
    
    person_data = Person.objects.get(id=person)
    
    return render_to_response('people/detail.html', {'person_data': person_data}, context_instance=RequestContext(request))
