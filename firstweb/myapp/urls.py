from django.urls import path
from myapp.views import *
from .views import BookListView, BookDetailView


urlpatterns = [
    path("", home, name="home-page"),
    path("blogs/", blog, name="blog-page"),
    path("blog/<int:id>/", blog_detail, name="blog-detail-page"),
    path("books/", BookListView.as_view(), name='book-list-page'),
    path("docs/", post_document_list, name='post-document-list-page'),
    path("doc/<slug:slug>/", post_document_detail, name='post-document-detail-page'), 
]
