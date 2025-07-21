from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from catalog.models import Product, Contact


def contact_list(request):
    latest_products = Product.objects.order_by("created_at")[:5]
    products = Product.objects.all()

    for product in latest_products:
        print(product)

    context = {"products": products}
    return render(request, "products_list.html", context)


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        return HttpResponse(f"Спасибо, {name}! Сообщение получено.")
    return render(request, "contacts.html")


def contact_view(request):
    contacts = Contact.objects.all()
    return render(request, "contacts.html", {"contacts": contacts})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, "product_detail.html", context)
