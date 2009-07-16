from django.db import models

class Storyline(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    description = models.TextField(blank=True)
    comics = models.ManyToManyField('nr_comics.Comic')
    
    class Meta:
        ordering = ('slug',)
    
    def __unicode__(self):
        return u"%s" % self.title
    
    def first(self):
        return self.comics.public().order_by('date')[0]
    
    def last(self):
        return self.comics.public().order_by('-date')[0]
        
    def associated_ids(self):
        return self.comics.public().order_by('date').values_list('sequence', flat=True)
