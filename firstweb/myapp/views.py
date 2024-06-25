from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Post, YoutubeVideo, Product, Order
from django.views.generic import ListView, DetailView
from .models import Book
from django.views import generic
from django.core.files.storage import FileSystemStorage


def home(request):
    # return HttpResponse("Hello : สวัสดี")
    all_post = Post.objects.all()
    all_youtube = YoutubeVideo.objects.all()

    context = {"all_youtube": all_youtube, "all_post": all_post}

    return render(request, "myapp/home.html", context)


def blog(request):
    all_post = Post.objects.all()

    context = {"all_post": all_post}

    return render(request, "myapp/blog.html", context)


def blog_detail(request, id):
    post = Post.objects.get(id=id)

    context = {"post": post}

    return render(request, "myapp/blog-detail.html", context)


def youtube(request):
    all_youtube = YoutubeVideo.objects.all()

    context = {"all_youtube": all_youtube}

    return render(request, "myapp/youtube.html", context)


class BookListView(ListView):
    model = Post
    template_name = "myapp/book-list.html"
    context_object_name = "books"


class BookDetailView(DetailView):
    model = Post
    template_name = "myapp/book-detail.html"
    context_object_name = "all_book"


def product_detail(request, slug):
    product = Product.objects.get(slug=slug)
    context = {"product": product, "product_price": product.normal_price}

    if product.price1 > 0:
        price_1 = (product.price1 * 100) / product.normal_price

        context["price_1"] = 100 - int(price_1)
        context["product_price"] = product.price1
    if product.price2 > 0:
        price_2 = (product.price2 * 100) / product.normal_price

        context["price_2"] = 100 - int(price_2)

    if request.method == "POST":
        data = request.POST.copy()

        new_order = Order()
        # new_order.user = product
        new_order.products = product
        new_order.first_name = data.get("first_name")
        new_order.last_name = data.get("last_name")
        new_order.tel = data.get("tel")
        new_order.email = data.get("email")
        new_order.address = data.get("address")
        new_order.count = data.get("count")
        new_order.buyer_price = data.get("buyer_price")
        new_order.shipping_cost = data.get("shipping_cost")
        
        try:
            file_image = request.FILES["upload_slip"]
            file_image_name = request.FILES["upload_slip"].name.replace(" ", "")
            file_system_storage = FileSystemStorage()
            file_name = file_system_storage.save(
                "products-slip/" + file_image_name, file_image
            )
            upload_file_url = file_system_storage.url(file_name)
            new_order.slip = upload_file_url[6:]
        except:
            new_order.slip = "/default.png"

        new_order.save()

    return render(request, "myapp/product-detail.html", context)
