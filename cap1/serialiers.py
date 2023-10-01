from rest_framework.serializers import ModelSerializer
from rest_framework.validators import ValidationError
from rest_framework.authtoken.models import Token
from .models import User, Tag


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


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name"]


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
