from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import *
from taggit.managers import TaggableManager


class Author(models.Model):
    author_name = models.CharField(max_length=100)
    avatar=models.ImageField(upload_to='avatar-images/', null=True, blank=True, default='default.png')
    
    def __str__(self):
        return self.author_name
    
class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=200, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    images = models.ImageField(upload_to='post-images/', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    date_updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=180, unique=True, null=True, blank=True)
    tags = TaggableManager()
        
    def __str__(self):
        return self.title

