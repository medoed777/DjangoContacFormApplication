from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, contact_view


app_name = CatalogConfig.name

urlpatterns = [
    path("", home, name="home"),
    path("contacts/", contacts, name="contacts"),
    path('contacts/', contact_view, name='contact_view'),
]
