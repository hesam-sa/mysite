from django.shortcuts import render,get_object_or_404

# Create your views here.

from django.http import HttpResponse,JsonResponse
from blog.models import Post
from django.utils import timezone
from next_prev import next_in_order, prev_in_order



def blog_view(request):
    now=timezone.now()
    post1=Post.objects.filter(status=1)
    post=post1.filter(published_date__lte=now)
    context = {'post':post}
    return render(request,'blog/blog-home.html',context)

def blog_single(request,pid):
    now=timezone.now()
    qs=Post.objects.filter(published_date__lte=now,status=1).order_by("pk")
    post=get_object_or_404(Post,pk=pid,published_date__lte=now,status=1)
    first= qs.first()
    last = qs.last()
    next = next_in_order(post,qs=qs)
    if next:
        nx=next
    else: nx=post
    prev = prev_in_order(post,qs=qs)
    if prev:
        pr=prev
    else: pr=post
    context = {'post':post,'next':nx,'prev':pr}
    return render(request,'blog/blog-single.html',context)
    
