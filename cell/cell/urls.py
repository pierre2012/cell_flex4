from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from static import views
from contact import views
from people import views
# from papers import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^myproject/', include('myproject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    
    
	url(r'^publications/', include('publications.urls')),
	url(r'^admin/publications/publication/import_bibtex/$', 'publications.admin_views.import_bibtex'),
    
    url(r'^admin/', include(admin.site.urls)),
    
)


urlpatterns += patterns('static.views',

    (r'^/$', 'homepage'),
    (r'^$', 'homepage'),

    (r'^about/$', 'about'),
    (r'about^$', 'about'),
    
    (r'^software/kolam/$', 'kolam'),
    (r'software/kolam^$', 'kolam'),
    
    (r'^software/firefly/$', 'firefly'),
    (r'software/firefly^$', 'firefly'),
    
    (r'^software/$', 'software'),
    (r'software^$', 'software'),

    (r'^resources/$', 'software'),
    (r'resources^$', 'software'),
    

    # (r'^research/$', 'research'),
    # (r'research^$', 'research'),
    # 
    # (r'^people/$', 'people'),
    # (r'people^$', 'people'),
    #     
    # (r'^publications/$', 'publications'),
    # (r'publications^$', 'publications'),
    #     

    #     
    # (r'^courses/$', 'courses'),
    # (r'courses^$', 'courses'),
    #     
    # (r'^calendar/$', 'calendar'),
#     (r'calendar^$', 'calendar'),
    #     
    # (r'^links/$', 'links'),
    # (r'links^$', 'links'),
    #     
    # (r'^images/$', 'images'),
    # (r'images^$', 'images'),

)

urlpatterns += patterns('contact.views',

	(r'^contact/$', 'contact'),
	(r'contact^$', 'contact'),

	(r'^contact/thankyou/$', 'thankyou'),
	(r'contact/thankyou^$', 'thankyou'),

)

urlpatterns += patterns('people.views',

	(r'people/$', 'people'),
	(r'people^$', 'people'),

	(r'^people/(?P<person>[-\w]+)/$', 'person_detail'),

)