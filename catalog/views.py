from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from catalog.models import Product, Contact


def home(request):
    latest_products = Product.objects.order_by('created_at')[:5]

    for product in latest_products:
        print(product)

    return render(request, "home.html", {'latest_products': latest_products})


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        return HttpResponse(f"Спасибо, {name}! Сообщение получено.")
    return render(request, "contacts.html")


def some_view(request):
    return reverse("contacts:home")


def contact_view(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts.html', {'contacts': contacts})
