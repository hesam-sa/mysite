from django.contrib import admin
from .models import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '***'
    # fields = ('title',)
    list_display = ('title','counted_view','status','created_date','updated_date','published_date')
    list_filter = ('status',)
    # ordering = ['created_date']
    search_fields = ['title','content']

admin.site.register(Post,PostAdmin)