from django.utils.safestring import mark_safe
from django.contrib import admin
from sreepuram.gallery.models import *
from sorl.thumbnail import *
from django.utils.safestring import mark_safe

ADMIN_THUMBS_SIZE = '60x60'

def add(list_, short_description=None, position=None, **kwargs):
  
    if short_description is not None:
        kwargs['short_description'] = short_description
    def decorate(f):
        if isinstance(f, basestring):
            list_.append(f)
        else:
            for key, value in kwargs.iteritems():
                setattr(f, key, value)
            if position is None:
                list_.append(f.__name__)
            else:
                list_.insert(position, f.__name__)
            return f
    return decorate

class CategoryImageAdmin(admin.ModelAdmin):

	prepopulated_fields={'slug':('title',)}
	list_display = ['order','title', 'image_category', 'date_created' ,'is_publish'] 
        list_filter = ('image_category', 'is_publish')

	@add(list_display, 'Image List', 0, allow_tags=True)
	def image_(self, obj):
		return mark_safe('<img width="100"  src="'+obj.url+'" />')


class CategoryAdmin(admin.ModelAdmin):

	prepopulated_fields={'slug':('title',)}
	list_display = ['category_name', 'date_created']

	@add(list_display, 'image_list', 0, allow_tags=True)
	def image_list(self, obj):
		return mark_safe('<img width="100"  src="'+obj.url+'" />')

admin.site.register(CategoryImage ,CategoryImageAdmin)
admin.site.register(Category ,CategoryAdmin)


