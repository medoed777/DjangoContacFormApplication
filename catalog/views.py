from django.http import HttpResponse
from django.shortcuts import render
from catalog.models import Product, Contact

from django.views.generic import ListView, DetailView
from django.views import View


class ProductsListView(ListView):
    model = Product
    template_name = "products_list.html"
    context_object_name = "products"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_products"] = Product.objects.order_by("created_at")[:5]
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detail.html"
    context_object_name = "product"


class ContactsView(View):
    template_name = "contacts.html"

    def get(self, request):
        return render(request, "contacts.html")

    def post(self, request):
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        return HttpResponse(f"Спасибо, {name}! Сообщение получено.")
