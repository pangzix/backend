from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics,status
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate

# Create your views here.

class UserCreate(generics.CreateAPIView):
    name = 'user_create'

    def get_authenticators(self):
        return ()

    def get_permissions(self):
        return ()

    def get_serializer_class(self):
        return UserSerializer

class LoginView(APIView):
    name = 'login'
    def get_permissions(self):
        return ()

    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username,password=password)

        if user:
            return Response(
                data={
                    'token':user.auth_token.key,
                }
            )
        else:
            return Response(
                data={
                    'error':'登陆失败',
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
