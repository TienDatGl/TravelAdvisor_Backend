from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from rest_framework.validators import ValidationError
from rest_framework.authtoken.models import Token
from .models import User, Tag, Location, Category, Trip, TripItem


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email", "username", "password", "avatar"]
        extra_kwargs = {
            'password': {'write_only': 'true'}
        }

    # def create(self, validated_data):
    #     user = User(**validated_data)
    #     user.set_password(validated_data['password'])
    #     user.save()
    #
    #     return user




class SignUpSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "username", "password"]
        extra_kwargs = {
            'password': {'write_only': 'true'}
        }

    def validate(self, attrs):
        email_exists = User.objects.filter(email=attrs['email']).exists()

        if email_exists:
            raise ValidationError("Email has already exists")

        return super().validate(attrs)

    def create(self, validated_data):
        password = validated_data.pop("password")

        user=super().create(validated_data)

        user.set_password(password)

        user.save()

        Token.objects.create(user=user)

        return user
    

class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name"]


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class LocationSerializer(ModelSerializer):
    tag = TagSerializer(many=True)
    category = CategorySerializer()

    class Meta:
        model = Location
        fields =['id', 'name', 'description', 'latitude', 'longitude','image', 'category', 'tag', 'address']


class TripItemSerializer(ModelSerializer):
    locations = LocationSerializer(many=True)

    class Meta:
        model = TripItem
        fields = ['id', 'day', 'locations']


class TripSerializer(ModelSerializer):
    items = TripItemSerializer(many=True)
    
    class Meta:
        model = Trip
        fields = ['id', 'name', 'days', 'user', 'items']



class TripItemCreateSerializer(ModelSerializer):
    locations = serializers.PrimaryKeyRelatedField(many=True, queryset=Location.objects.all())
    # trip = TripSerializer()

    class Meta:
        model = TripItem
        fields = ['id', 'day', 'locations', 'trip']



class TripCreateSerializer(ModelSerializer):
    items = TripItemCreateSerializer(many=True)

    class Meta:
        model = Trip
        fields = ['id', 'name', 'days', 'user', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        trip = Trip.objects.create(**validated_data)

        trip_items = []  # Danh sách để lưu các TripItem

        for item_data in items_data:
            locations_data = item_data.pop('locations')
            item_data['trip'] = trip  
            trip_item = TripItem.objects.create(**item_data)

            for location in locations_data:
                trip_item.locations.add(location)

            trip_items.append(trip_item)  

        return trip




   