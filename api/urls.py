from django.urls import path
from .views import *

urlpatterns = [
    path('', api_all_links, name='api-all-links'),
    path('all-books/', allBooks, name='api-allbooks'),
    path('book/<int:id>/', book, name='api-onebook'),
    path('create-book/', create_book, name='api-create-book'),
    path('update-book/<int:id>/', update_book, name='api-update-book'),
    path('delete-book/<int:id>/', delete_book, name='api-delete-book'),
]
