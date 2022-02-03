from enum import unique
from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import get_user_model
from rest_framework import authentication


User = get_user_model()
class RegisterSerilalizer(serializers.ModelSerializer):
    
    email = serializers.EmailField(max_length=200)
    username = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=200)


    

    class Meta:
        model = User

        fields = ('email', 'username', 'password',)
        
    
    def validate(self, attrs):
        
        email_exists = User.objects.filter(email=attrs("email").exists())
        if email_exists:
            raise serializers.ValidationError(detail='email already exists!')


        username_exists = User.objects.filter(username=attrs('username').exists())
        if username_exists:
            raise serializers.ValidationError(detail='username already exists')


        return super().validate(attrs)

    
   
class LoginSerializers(serializers.ModelSerializer):

    class Meta:
        model = User

        email = serializers.CharField(max_length=200)
        username = serializers.CharField(max_length=200)
        password = serializers.CharField(max_length=200)

    def validate(self, data):
        email = data.get('email', None)
        username = data.get('username', None)
        password = data.get('password', None)

        if email and username and password:

            user = authentication(email=email, password=password)
            if user:
                data['user'] = user

            
        return data