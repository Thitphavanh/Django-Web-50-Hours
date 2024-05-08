from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import *
from taggit.managers import TaggableManager
from shortuuid.django_fields import ShortUUIDField
from embed_video.fields import EmbedVideoField
class Author(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="author-image/", null=True, blank=True, default='default.png')

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
    yid = ShortUUIDField(unique=True, length=10, max_length=20,
                         prefix="yid", alphabet="abcdefgh12345")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=180)
    video_url = EmbedVideoField(null=True, blank=True)
    description = models.TextField(max_length=280, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)
    slug = models.SlugField(unique=True, max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-date_created']
    
    
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