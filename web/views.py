from django.http import HttpResponse
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets, generics
from web.serializers import GroupSerializer, UserSerializer
from django.http import JsonResponse
from django.contrib.auth import authenticate, login

from .models import MainUser
from .serializers import MainUserSerializer





class MainUserCreateAPIView(generics.CreateAPIView):
    queryset = MainUser.objects.all()
    serializer_class = MainUserSerializer


# Create your views here.


def create_user(request):
    if request.method == 'POST':
        request_data = json.loads(request.body)
        first_name = request_data['first_name']
        username = request_data['username']
        email = request_data['email']
        password = request_data['password']

        # بررسی اینکه آیا یوزری با این نام کاربری یا ایمیل قبلاً وجود دارد یا خیر
        if User.objects.filter(Q(username=username) | Q(email=email)).exists():
            return JsonResponse({'error': 'Username or email already exists'}, status=400)

        # ایجاد یوزر جدید
        new_user = User.objects.create(
            name=name,
            username=username,
            email=email,
            set_password=password
        )

        # ورود خودکار کاربر
        authenticated_user = authenticate(username=username, password=password)
        if authenticated_user:
            login(request, authenticated_user)
            return JsonResponse({'message': 'User created and logged in successfully'}, status=201)

        return JsonResponse({'error': 'Unable to create user'}, status=500)





#REST fucking bullshit about API 


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

