from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from settings import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sitioweb.views.home', name='home'),
    # url(r'^sitioweb/', include('sitioweb.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^$', 'sitio.views.index'),
    url(r'^sitio/', include('sitio.urls')),
    url(r'^foro/', include('askbotmini.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tagging_autocomplete/', include('tagging_autocomplete.urls')),
    url(r'^comunidades/', 'sitio.views.comunidades'),

)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()

if DEBUG:
    urlpatterns += patterns('',
                (r'^uploads/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
                )
