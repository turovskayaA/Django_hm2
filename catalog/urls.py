from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ProductView, ProductUpdateView, ProductCreateView, \
    ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('contacts/', ProductView.as_view(), name='contacts'),
    path('', ProductListView.as_view(), name='home'),
    path('view/<int:pk>/', ProductDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', ProductUpdateView.as_view(), name='edit'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete'),
]
