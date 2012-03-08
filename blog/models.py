from django.db import models
from django.contrib.auth.models import User
from sreepuram.widgets import RemovableImageField
from datetime import datetime
from django.db.models.query import QuerySet
from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^sreepuram.widgets\.RemovableImageField"])
    
class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = 'Categories'
        
    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "blog/%s/" % ( self.slug )
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    image = RemovableImageField(upload_to='uploads/images/blog/', null=True, blank=True)
    categories = models.ManyToManyField(Category)
    content = models.TextField()
    publish = models.BooleanField()
    publish_date = models.DateTimeField(default=datetime.now())
    author = models.ForeignKey(User, null=True, blank=True)
    
    class Meta:
        ordering = ['-publish_date',]
        
    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return "blog/%s/%s/" % ( self.categories.all()[0].slug, self.slug )

class CommentManager(models.Manager):
    def count(self):
        return self.filter(approve=True).count()

class Comment(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User)
    post = models.ForeignKey(Post)
    approve = models.BooleanField(default=False)
    submit_date = models.DateTimeField(default=datetime.now())
    objects = CommentManager()

    def __unicode__(self):
        return self.content[20:]
