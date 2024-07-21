from django import template
from blog.models import Post

register = template.Library()

@register.simple_tag(name='posts')
def function():
    posts = Post.objects.filter(status=1)
    return  posts

@register.filter
def snppets(value,arg=20):
    return value[:arg] + '...'

@register.inclusion_tag('popularpost.html')
def popularposts():
    posts = Post.objects.filter(status=1).order_by('-published_date')[:2]
    return {'posts':posts}