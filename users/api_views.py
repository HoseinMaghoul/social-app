from django.shortcuts import render
from rest_framework.views import APIView
from .models import CustomUser
from .serializer import RegisterSerilalizer, LoginSerializers
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from permissions import IsOwnerOrReadOnly
from rest_framework import authentication
from rest_framework.permissions import AllowAny
from django.contrib.auth import login



class RegisterApiView(APIView):
    
    permission_classes = (AllowAny,)

    def post(self, request):
        user = request.data
        serializer = RegisterSerilalizer(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)



class LoginApiView(APIView):

    permission_class = (AllowAny,)



    def post(self, request):
        serializer = LoginSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        
        return Response(status = status.HTTP_200_OK)

