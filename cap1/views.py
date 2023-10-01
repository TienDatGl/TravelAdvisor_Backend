from django.contrib.auth import authenticate
from rest_framework import viewsets, permissions, status, generics, request
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import User
from .serialiers import UserSerializer, TagSerializer, SignUpSerializer
from .tokens import create_jwt_pair_for_user


# Create your views here.


class UserViewset(viewsets.ViewSet,
                  generics.ListAPIView,
                  generics.CreateAPIView,
                  generics.DestroyAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer
    passer_classes = [MultiPartParser]

    # def create(self, request):
    #     serializer = self.get_serializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         response_data = {'message': 'Đăng ký thành công', 'data': serializer.data, 'alert': True}
    #         return Response(response_data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SignUpViewset(generics.GenericAPIView):
    permission_classes = []
    serializer_class = SignUpSerializer

    def post(self, request: Request):
        data = request.data

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()

            response = {
                'message': 'Create Successfully',
                'data': serializer.data,
                'status': True
            }

            return Response(data=response, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginViewset(APIView):
    permission_classes = []
    def post(self, request: Request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            tokens=create_jwt_pair_for_user(user)
            response = {
                'message': "Login Success",
                "token": tokens,
                'user': user.username
            }
            return Response(data=response, status=status.HTTP_200_OK)

        else:
            return Response(data={'error': 'Invalid email or password'})

    def get(self, request: Request):
        content = {
            "user": str(request.user),
            "auth": str(request.auth)
        }

        return Response(data=content, status=status.HTTP_200_OK)

# def index(request):
#     return render(request, template_name='index.html', context={
#         'name': 'Dat'
#     })
