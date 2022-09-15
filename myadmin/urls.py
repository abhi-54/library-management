from django.urls import path
from .views import *

urlpatterns = [
    path('', admin_signup, name='admin-signup'),
    path('login/', admin_login, name='admin-login'),
    path('admin-dashboard/', admin_dashboard, name='admin-dashboard')
]
