from django.conf import settings
from django.core.cache import cache

from catalog.models import Product, Category


def get_cache_product():
    if settings.CACHE_ENABLED:
        key = f'product_list'
        product_list = cache.get(key)
        if product_list is None:
            product_list = Product.objects.all()
            cache.set(key, product_list)
    else:
        product_list = Product.objects.all()
    return product_list


def get_cache_categories():
    if settings.CACHES_ENABLED:
        key = 'category_list'
        category_list = cache.get(key)
        if category_list is None:
            category_list = Category.objects.all()
            cache.set(key, category_list)
    else:
        category_list = Category.objects.all()
    return category_list
