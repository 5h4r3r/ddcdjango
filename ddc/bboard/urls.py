from django.urls import path

from .views import index, api

urlpatterns = [
    path('', index),
    path('api/', api),
]
