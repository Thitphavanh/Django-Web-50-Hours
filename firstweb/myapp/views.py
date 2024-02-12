from django.shortcuts import render
# from django.http import HttpResponse
from .models import *


def home(request):
    # return HttpResponse("Hello world!")
    all_post = Post.objects.all()
    
    context = {'all_post': all_post}
    
    return render(request,'myapp/home.html', context)