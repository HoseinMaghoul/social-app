from asyncore import read
from dataclasses import fields
from unittest import result
from rest_framework import serializers
from .models import Comment
from post.models import Post






class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'






class PostSerilaizer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)


    class Meta:
        model = Post
        fields = '__all__'

  

