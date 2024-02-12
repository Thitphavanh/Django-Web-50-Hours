from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'author_name', 'avatar']
    list_editable =['author_name']


admin.site.register(Author, AuthorAdmin)
    
    
class PostAdmin(SummernoteModelAdmin):
    list_display =['id', 'title', 'images']
    list_editable =['title']


admin.site.register(Post, PostAdmin)