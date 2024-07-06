
from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    
    path('blog/',blog_view,name='index'),
    path('blog/single',blog_single,name='single'),
   
]
