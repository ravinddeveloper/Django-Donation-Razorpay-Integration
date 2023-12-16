from django.urls import path,include
from .views import *
urlpatterns = [
    path('', index),
    path('success/',success),
    path('failed/',fail),
]
