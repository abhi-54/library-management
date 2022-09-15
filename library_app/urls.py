from django.urls import path
from .views import *

urlpatterns = [
    path('', test_view, name='start'),
]
