from django import template
from blog.models import Post,Category
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

@register.inclusion_tag('blog/blog-post-categories.html')
def postcategories():
    now=timezone.now()
    posts = Post.objects.filter(status=1,published_date__lte=now)
    categories = Category.objects.all()
    cat_dict ={}
    for name in categories:
        cat_dict[name]=posts.filter(category=name).count()
    return {'categories':cat_dict}

@register.inclusion_tag('website/latestpost.html')
def latest():
    now=timezone.now()
    posts = Post.objects.filter(status=1,published_date__lte=now).order_by('published_date')[:6]
    return {'posts':posts}
    
    
    