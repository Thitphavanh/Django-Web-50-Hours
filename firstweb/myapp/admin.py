from django.contrib import admin
from .models import Post, Author, YoutubeVideo, Book, Product, Category, Order
from django_summernote.admin import SummernoteModelAdmin


class AuthorAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "image"]
    list_editable = ["name"]


admin.site.register(Author, AuthorAdmin)


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ("body",)
    list_display = ["id", "title", "images"]
    list_editable = ["title"]


admin.site.register(Post, PostAdmin)


class YoutubeVideoAdmin(SummernoteModelAdmin):
    summernote_fields = ("body",)
    list_display = ["id", "author", "title"]
    list_editable = ["title"]


admin.site.register(YoutubeVideo, YoutubeVideoAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "author"]
    list_editable = ["title"]


admin.site.register(Book, BookAdmin)


class ProductAdmin(SummernoteModelAdmin):
    summernote_fields = ("detail",)
    list_display = ["id", "shipping_cost", "available"]


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Order)
