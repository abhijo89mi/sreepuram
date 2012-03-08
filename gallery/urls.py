from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

urlpatterns = patterns('gallery.views',
       
    (r'^$', 'index'),
    (r'^gallery/(?P<name>[-\w]+)/$','gallery'),
    
    
)
