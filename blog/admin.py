from django.contrib import admin
from blog.models import Post,Category
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '***'
    # fields = ('title',)
    list_display = ('title','counted_view','status','created_date','updated_date','published_date')
    list_filter = ('status',)
    # ordering = ['created_date']
    search_fields = ['title','content']
    summernote_fields = ('content',)
    
admin.site.register(Category)
admin.site.register(Post,PostAdmin)