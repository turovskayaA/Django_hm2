from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts, home, base_product, product_pk

app_name = CatalogConfig.name

urlpatterns = [
    path('contacts/', contacts, name='contacts'),
    path('', home, name='home'),
    path('base_product/', base_product, name='base_product'),
    path('<int:pk>/', product_pk, name='product_pk'),
]
