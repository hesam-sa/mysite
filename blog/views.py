from django.shortcuts import render,get_object_or_404

# Create your views here.

from django.http import HttpResponse,JsonResponse
from blog.models import Post
import datetime

# 
# context = {'posts':post}

def blog_view(request):
    return render(request,'blog/blog-home.html',context)

def blog_single(request):
    return render(request,'blog/blog-single.html')

def test(request):
    now=datetime.datetime.now()
    post = Post.objects.filter(published_date__lte=now)
    # post = Post.objects.filter(status=1)
    context = {'post':post,'now':now}
    return render(request,'test.html',context)
