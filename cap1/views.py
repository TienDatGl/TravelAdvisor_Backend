from django.contrib.auth import authenticate
from rest_framework import viewsets, permissions, status, generics, request
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import User, Location, Trip, TripItem
from .serialiers import UserSerializer, TagSerializer, SignUpSerializer, LocationSerializer, TripCreateSerializer, TripSerializer
from .tokens import create_jwt_pair_for_user




# Create your views here.

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
        user_serializer = UserSerializer(user)

        if user is not None:
            tokens=create_jwt_pair_for_user(user)
            response = {
                'message': "Login Success",
                "token": tokens,
                'user': user_serializer.data
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


class UserViewset(viewsets.ViewSet,
                  generics.ListAPIView,
                  generics.CreateAPIView,
                  generics.DestroyAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer
    passer_classes = [MultiPartParser]


class LocationViewset(viewsets.ViewSet,
                      generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    parser_classes = [MultiPartParser]


class TripViewSet(viewsets.ViewSet,
                  generics.ListAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer



class TripCreateViewSet(APIView):
   

    def post(self, request: Request):
        trip_data = request.data
        trip_serializer = TripCreateSerializer(data=trip_data)
        print(trip_data)

        if trip_serializer.is_valid():
            trip =trip_serializer.save()

            # items = trip_data.get('items', [])
            # for item_data in items:
            #     trip_item = TripItem.objects.create(
            #         day = item_data['day'],
            #         trip = trip
            #     )
            #     trip_item.locations.set(item_data['locations'])

            #     print(trip_serializer.data)
               
            
            response = {
                'message': 'Create successfully',
                'data': trip_serializer.data
            }

            return Response(data=response, status=status.HTTP_201_CREATED)

        return Response(trip_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserTripsViewSet(APIView):
    def get(self, request):
        user_id = request.GET.get('user_id')
        try:
            user_trips = Trip.objects.filter(user=user_id)
            serializer_class = TripSerializer(user_trips, many=True)
            
            response = {
                'message': 'Get trips of the user successfully',
                'data': serializer_class.data
            }
            return Response(data=response, status=status.HTTP_200_OK) 
        except Trip.DoesNotExist:
            return Response({'message': 'User has no trips.'}, status=status.HTTP_404_NOT_FOUND)


    


    





