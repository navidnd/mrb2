from django.urls import path
from . import views


urlpatterns = [
    path('movementadd/', views.MovementAdd, name='MovementAdd'),

    path('register', views.register_view, name='register'),
    path('login', views.login_view, name='login'),
    # دیگر الگوهای آدرس مربوط به حساب‌ها
]
