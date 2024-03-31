from django.urls import path
from . import views


urlpatterns = [
    path('Move', views.My_Movement_view, name='Move'),

    path('register', views.register_view, name='register'),
    path('login', views.login_view, name='login'),
    # دیگر الگوهای آدرس مربوط به حساب‌ها
]
