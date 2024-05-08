from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Post, YoutubeVideo
from django.views.generic import ListView, DetailView
from .models import Book
from django.views import generic
from markdownx.utils import markdownify



def home(request):
    # return HttpResponse("Hello : สวัสดี")
    all_post = Post.objects.all()
    all_youtube = YoutubeVideo.objects.all()

    context = {"all_youtube" : all_youtube, "all_post": all_post}

    return render(request, "myapp/home.html", context)


def blog(request):
    all_post = Post.objects.all()

    context = {"all_post": all_post}

    return render(request, "myapp/blog.html", context)




def youtube(request):
    all_youtube = YoutubeVideo.objects.all()

    context = {"all_youtube" : all_youtube}

    return render(request, "myapp/youtube.html", context)




class BookListView(ListView):
    model = Post
    template_name = 'myapp/book-list.html'
    context_object_name = 'books'
    


class BookDetailView(DetailView):
    model = Post
    template_name = 'myapp/book-detail.html'
    context_object_name = 'all_book'
    
    
    
    
def post_document_list(request):
    documents = Post.objects.all()
    context = {'documents': documents}
    
    return render(request, 'myapp/post-document-list.html',context)


def post_document_detail(request, slug):
    document = Post.objects.get(slug=slug)
    context = {'document': document} 
    
    return render(request, 'myapp/post-document-detail.html',)