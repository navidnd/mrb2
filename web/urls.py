from django.urls import path
from .views import MainUserCreateAPIView



urlpatterns = [

    path('api/create_user/', MainUserCreateAPIView.as_view(), name='create_user'),

    #path('login', views.login, name='login'),
    #path('register', views.register, name='register'),
    #path('dashboard', views.dashboard, name='dashboard'),

]
