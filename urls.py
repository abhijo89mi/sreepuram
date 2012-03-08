from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sreepuram.views.home', name='home'),
    # url(r'^sreepuram/', include('sreepuram.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

# Main urls ...

urlpatterns += patterns('sreepuram.main',

	url(r'^$','views.index',name='home'),
)

#Gallery
urlpatterns += patterns('sreepuram.gallery.views',
	url(r'^gallery-index/$', 'index',name='galleryindex'),
	(r'^gallery/(?P<name>[-\w]+)/$','gallery'),

)
#Blog
urlpatterns += patterns('sreepuram.blog.views',
	url(r'^blog-index/$', 'index',name='blogindex'),
	url(r'^(?P<category>[-\w]+)/$', 'category_posts', name="category_posts"),
	url(r'^(?P<category>[-\w]+)/(?P<post>[-\w]+)/$', 'post', name="blog_post"),

)
