from django.contrib import admin
from .models import contact,NewsLetter

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','email','subject','created_date','updated_date']
    list_filter = ('email',)
    search_fields = ('name','meesage')
    date_hierarchy = 'created_date'
    

admin.site.register(contact,ContactAdmin)
admin.site.register(NewsLetter)