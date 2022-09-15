from django.urls import path, re_path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', student_signup, name='student-signup'),
    path('login/', student_login, name='student-login'),
    path('student-dashboard/', student_dashboard, name='student-dashboard'),
    re_path('student-logout/', LogoutView.as_view(), {'next_page': '/student/login/'}, name='student-logout')
]
