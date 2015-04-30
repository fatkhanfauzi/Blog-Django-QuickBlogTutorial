from django.db import models
from ckeditor.fields import RichTextField
from django.core.urlresolvers import reverse

class Tag(models.Model):
    slug = models.SlugField(max_length=200, unique=True)
    def __str__(self):
        return self.slug

class EntryQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)

class Entry(models.Model):
    title = models.CharField(max_length=200)
    body = RichTextField()
    slug = models.SlugField(max_length=200, unique=True)
    publish = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag)
    
    objects = EntryQuerySet.as_manager()

    def get_absolute_url(self):
        return reverse("entry_detail", kwargs={"slug": self.slug})
        
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Blog Entry"
        verbose_name_plural = "Blog Entries"
        ordering = ["-created"]

class CommentQuerySet(models.QuerySet):
    def sort_asc_by_created(self, direction):
        if direction == True:
            return self.objects.order_by('-created')
        else:
            return self.objects.order_by('created')
       
class Comment(models.Model):
    entry = models.ForeignKey(Entry)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    comment = RichTextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    objects = CommentQuerySet.as_manager()
    
    def __str_(self):
        return self.comment
    