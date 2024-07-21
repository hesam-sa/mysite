from django import template
from blog.models import Post
from django.utils import timezone

register = template.Library()

@register.simple_tag(name='posts')
def function():
    posts = Post.objects.filter(status=1)
    return  posts

@register.filter
def snppets(value,arg=20):
    return value[:arg] + '...'

@register.inclusion_tag('blog/blog-popularposts.html')
def latestposts():
    now=timezone.now()
    posts = Post.objects.filter(status=1,published_date__lte=now).order_by('published_date')[:5]
    return {'posts':posts}