from django.urls import path
from . import views


urlpatterns = [
    path('My_Movement', views.My_Movement_view, name='My_Movement'),

    path('register', views.register_view, name='register'),
    path('login', views.login_view, name='login'),
    # دیگر الگوهای آدرس مربوط به حساب‌ها
]
