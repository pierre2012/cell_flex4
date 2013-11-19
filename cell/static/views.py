from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.http import Http404
from django.core.urlresolvers import reverse
from django.conf.urls.defaults import *


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core import serializers

from django.contrib.auth.decorators import login_required



def homepage(request):
    
    return render_to_response('static/homepage.html')


def about(request):
    
    return render_to_response('static/about.html')


def research(request):
    
    return render_to_response('static/research.html')

def people(request):
    
    return render_to_response('static/people.html')


def publications(request):
    
    return render_to_response('static/publications.html')


def presentations(request):
    
    return render_to_response('static/presentations.html')




def courses(request):
    
    return render_to_response('static/courses.html')


def calendar(request):
    
    return render_to_response('static/calendar.html')


def links(request):
    
    return render_to_response('static/links.html')
    
    
def images(request):
    
    return render_to_response('static/images.html')
    
    
    
    

def software(request):
    
    return render_to_response('static/software.html')


def firefly(request):
    
    return render_to_response('static/firefly.html')


def kolam(request):
    
    return render_to_response('static/kolam.html')





import watson

def search(request):
    
    search_results = ''
    
    if ('q' in request.GET) and request.GET['q'].strip():
        
        query_string = request.GET['q']
        
    	search_results = watson.search(query_string)    
    
    	return render_to_response('static/search.html', {'search_results': search_results}, context_instance=RequestContext(request))

    return render_to_response('static/search.html', context_instance=RequestContext(request))




