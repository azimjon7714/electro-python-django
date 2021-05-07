from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', base_view, name='base'),
]
