from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.models import Post, YoutubeVideo, Product, Order, TrackingOrderID
from django.views.generic import ListView, DetailView
from .models import Book
from django.views import generic
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
import string
import random


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


# Create random order id
def random_order_id():
    ro_id = ""
    ro_id += random.choice(string.ascii_uppercase)
    ro_id += random.choice(string.ascii_uppercase)

    for i in range(5):
        ro_id += random.choice("0123456789")

    return ro_id


def product_detail(request, slug):
    random_order_id()

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
        
        
        # Add new tracking id
        try:
            tracking_id = TrackingOrderID.objects.all()
            while True:
                order_ID = random_order_id()
                for tid in tracking_id:
                    if order_ID == tid.order_id:
                        continue
                break

        except:
            order_ID = random_order_id()

        new_tracking_id = TrackingOrderID()
        new_tracking_id.tracking_order = new_order
        new_tracking_id.order_id = order_ID
        new_tracking_id.save()

        return redirect("tracking-order-id-page", order_ID)

    return render(request, "myapp/product-detail.html", context)


def tracking_order_id(request, tid):
    tracking_id = TrackingOrderID.objects.get(order_id=tid).tracking_order
    buyer_price = tracking_id.buyer_price

    if buyer_price == int(buyer_price):
        buyer_price = int(buyer_price)

    shipping_cost = tracking_id.shipping_cost
    if shipping_cost == int(shipping_cost):
        shipping_cost = int(shipping_cost)

    all_price = tracking_id.buyer_price + tracking_id.shipping_cost

    context = {
        "tracking_id": tracking_id,
        "buyer_price": buyer_price,
        "order_id": tid,
        "shipping_cost": shipping_cost,
        "all_price": all_price,
    }
    return render(request, "myapp/tracking-order.html", context)
