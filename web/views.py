from django.shortcuts import render
from django.http import HttpResponse




# Create your views here.


def register_view(request):
    print('user registered')


def login_view(request):
    print('login')


def My_Movement_view(request):
    data = {'success': True}
    return HttpResponse(data)


