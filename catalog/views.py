from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse


def home(request):
    return render(request, "home.html")


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        return HttpResponse(f"Спасибо, {name}! Сообщение получено.")
    return render(request, "contacts.html")


def some_view(request):
    return reverse("contacts:home")
