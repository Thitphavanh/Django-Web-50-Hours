from django.contrib import admin
from .models import Post, Author, YoutubeVideo, Book
from django_summernote.admin import SummernoteModelAdmin


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image']
    list_editable = ['name']


admin.site.register(Author, AuthorAdmin)


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('body',)
    list_display = ['id', 'title', 'images']
    list_editable = ['title']


admin.site.register(Post, PostAdmin)



class YoutubeVideoAdmin(SummernoteModelAdmin):
    summernote_fields = ('body',)
    list_display = ['id', 'author', 'title']
    list_editable = ['title']


admin.site.register(YoutubeVideo, YoutubeVideoAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author']
    list_editable = ['title']


admin.site.register(Book, BookAdmin)