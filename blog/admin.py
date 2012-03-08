from sreepuram.blog.models import *
from django.contrib import admin

class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'content']
    list_display = ('title', 'publish', 'publish_date', 'author')
    prepopulated_fields = {"slug": ("title",)}
    #exclude = ('author', )
    list_filter = ('categories', 'author')
    
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()

class CommentAdmin(admin.ModelAdmin):
    list_display = ('title', 'approve', 'author', 'post')
    
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category)
