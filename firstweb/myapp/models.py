from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import *
from taggit.managers import TaggableManager
from shortuuid.django_fields import ShortUUIDField
from embed_video.fields import EmbedVideoField


class Author(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(
        upload_to="author-image/", null=True, blank=True, default="default.png"
    )

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=280, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    images = models.ImageField(upload_to="post-images/", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    date_updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, max_length=180, null=True, blank=True)
    tags = TaggableManager()

    def __str__(self):
        return self.title


class YoutubeVideo(models.Model):
    yid = ShortUUIDField(
        unique=True, length=10, max_length=20, prefix="yid", alphabet="abcdefgh12345"
    )
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=180)
    video_url = EmbedVideoField(null=True, blank=True)
    description = models.TextField(max_length=280, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    slug = models.SlugField(unique=True, max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-date_created"]


class OurWork(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=280, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    images = models.ImageField(upload_to="our-work-images/", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    date_updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, max_length=180, null=True, blank=True)
    tags = TaggableManager()

    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    published_date = models.DateField()


class Category(models.Model):
    category_name = models.CharField(max_length=255, default="หมวดหมู่ทั่วไป")
    category_detail = models.TextField(max_length=100, unique=True)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True
    )
    name = models.CharField(max_length=255)
    introduction = models.TextField(null=True, blank=True)
    detail = models.TextField(null=True, blank=True)
    normal_price = models.IntegerField(null=True, blank=True)
    price1 = models.IntegerField(null=True, blank=True)
    price2 = models.IntegerField(null=True, blank=True)
    shipping_cost = models.IntegerField(default=40, null=True, blank=True)
    images = models.ImageField(upload_to="products/", null=True, blank=True)
    quantity = models.IntegerField(default=1)
    available = models.BooleanField(default=True)
    unit = models.CharField(max_length=255, default="-")
    image_url = models.CharField(max_length=255, null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    tel = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    address = models.TextField(null=True, blank=True)
    count = models.IntegerField(default=1)
    buyer_price = models.FloatField(default=0)
    shipping_cost = models.FloatField(default=0)
    slip = models.ImageField(upload_to="products-slip/", null=True)

    # def __str__(self):
    #     return self.first_name
