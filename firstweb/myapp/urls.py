from django.urls import path
from myapp.views import *
from .views import BookListView, BookDetailView, product_detail


urlpatterns = [
    path("", home, name="home-page"),
    path("blogs/", blog, name="blog-page"),
    path("blog/<int:id>/", blog_detail, name="blog-detail-page"),
    path("books/", BookListView.as_view(), name="book-list-page"),
    path("product/<slug:slug>/", product_detail, name="product-detail-page"),
]
