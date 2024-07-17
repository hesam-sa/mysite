from django.shortcuts import render,get_object_or_404

# Create your views here.

from django.http import HttpResponse,JsonResponse
from blog.models import Post
from django.utils import timezone



def blog_view(request):
    now=timezone.now()
    post1=Post.objects.filter(status=1)
    post=post1.filter(published_date__lte=now)
    context = {'post':post}
    return render(request,'blog/blog-home.html',context)

def blog_single(request,pid):
    now=timezone.now()
    post1=Post.objects.filter(status=1)
    post2=post1.filter(published_date__lte=now)
    post=get_object_or_404(post2,pk=pid)
    post.counted_view += 1
    post.save()
    context = {'post':post}
    return render(request,'blog/blog-single.html',context)