from django.contrib import admin
from blog.models import Post,Category,Comment
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

class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '***'
    # fields = ('title',)
    list_display = ('post','name','approved','created_date',)
    list_filter = ('post','approved',)
    # ordering = ['created_date']
    search_fields = ['title','content']
    
    

    
admin.site.register(Category)
admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)