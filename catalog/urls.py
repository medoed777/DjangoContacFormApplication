from django.urls import path
from catalog.apps import CatalogConfig
from .views import ProductsListView, ProductDetailView, ContactsView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductsListView.as_view(), name="products_list"),
    path("product_create/", ProductCreateView.as_view(), name="product_create"),
    path("product_update/<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"),
    path("product_update/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
]
