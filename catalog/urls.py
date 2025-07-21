from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import contacts, contact_view, contact_list, product_detail


app_name = CatalogConfig.name

urlpatterns = [
    path("", contact_list, name="contact_list"),
    path("contacts/", contacts, name="contacts"),
    path("contacts/", contact_view, name="contact_view"),
    path("product_detail/<int:pk>/", product_detail, name="product_detail"),
]
