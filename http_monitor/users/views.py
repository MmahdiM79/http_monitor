from django.shortcuts import render

# Create your views here.
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from rest_framework import (
    serializers,
    generics,
)
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny,
)

from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=True,
        validators=[
            UniqueValidator(queryset=User.objects.all())
        ]
    )
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password')

    def create(self, validated_data):
        try:
            password = validated_data.pop('password')
            user = User.objects.create(**validated_data)
            user.set_password(password)
            user.save()
            return user
        except Exception:
            raise serializers.ValidationError(
                {
                    "message": 'There is something wrong during your registration. Please try again later'
                }
            )


class UserAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class RegisterApi(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication,]
