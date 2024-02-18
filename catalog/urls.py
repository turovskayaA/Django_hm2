from django.urls import path

from catalog.views import contacts, index

urlpatterns = [
    path('contacts/', contacts),
    path('', index)
]
