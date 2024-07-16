from django.shortcuts import render,get_object_or_404

# Create your views here.

from django.http import HttpResponse,JsonResponse
from blog.models import Post
import datetime



def blog_view(request):
    post=Post.objects.filter(status=1)
    context = {'post':post}
    return render(request,'blog/blog-home.html',context)

def blog_single(request,pid):
    post=get_object_or_404(Post,pk=pid)
    context = {'post':post}
    return render(request,'blog/blog-single.html',context)

def test(request):
    now=datetime.datetime.now()
    post = Post.objects.filter(published_date__lte=now)
    context = {'post':post,'now':now}
    return render(request,'test.html',context)

def test2(request,pid):
    post= Post.objects.get(id=pid)
    post.counted_view += 1
    post.save()
    context={'post':post}
    return render(request,'test2.html',context)

def test3(request,pid):
    post = Post.objects.get(id=pid)
    context={'post':post}
    return render(request,'test2.html',context)

    