from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import SafeString
from django.template.defaultfilters import stringfilter
from django import template




# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name
    
class Post(models.Model):
    image = models.ImageField(upload_to='blog/',default='blog/default.jpg')
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    # tag
    category = models.ManyToManyField(Category)
    counted_view = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True)
    
    class Meta:
        # verbose_name = 'ok'
        ordering = ['created_date']

    def __str__(self):
        return self.name 
    
    def snippets(self):
        return self.content[:100] +'...'
    
    
    def count_words(self):
        words = self.content.split()
        if len(words) > 20:
            return ' '.join(words[:20]) + '...'
        else: 
            return self.content