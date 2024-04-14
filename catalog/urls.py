from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ProductView, ProductUpdateView, ProductCreateView, \
    ProductDeleteView, CategoryListView

app_name = CatalogConfig.name

urlpatterns = [
    path('contacts/', ProductView.as_view(), name='contacts'),
    path('', cache_page(60)(ProductListView.as_view()), name='home'),
    path('view/<int:pk>/', ProductDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', ProductUpdateView.as_view(), name='edit'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete'),
    path('categories_list/', cache_page(60)(CategoryListView.as_view()), name='list_category'),
]
