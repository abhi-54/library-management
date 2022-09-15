from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth.views import LogoutView
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myadmin.urls')),
    path('student/', include('student.urls')),
    path('api/', include('api.urls')),
    re_path('logout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
]
