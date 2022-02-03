from functools import partial
from statistics import mode
from sys import api_version
from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import PostSerilaizer, CommentSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Comment
from post.models import Post
from rest_framework.permissions import IsAuthenticated
from permissions import IsOwnerOrReadOnly
# Create your views here.


class PostListView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        srz_data = PostSerilaizer(instance=posts, many=True)
        return Response(srz_data, status=status.HTTP_200_OK)



class PostCreateView(APIView):
    permission_classes = [IsAuthenticated,]

    def post(self, request):
        data = PostSerilaizer(data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data, status=status.HTTP_201_CREATED)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)



class PostUpdateView(APIView):
    permission_classes = [IsOwnerOrReadOnly,]


    def put(self, request, pk):
        post = Post.objects.get(pk=pk)
        self.check_object_permissions(request, post)
        srz_data = PostSerilaizer(instance=post, data=request.data, partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_201_CREATED)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)



class PostDeleteView(APIView):
    permission_classes = [IsOwnerOrReadOnly,]


    def delete(self, request, pk):
        post = Post.objects.get(pk=pk)
        self.check_object_permissions(request, post)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentListView(APIView):
    model = Comment
    # template_name = 'comments_detail.html'


    def get(self,request, slug):
        comments = Comment.objects.all(slug=slug)
        # queryset = ReplayComment.objects.filter(is_published=0,comments=comments).distinct()
        srz_data = CommentSerializer(instance=comments, many=True)
        return Response(srz_data, status=status.HTTP_200_OK)




class CommentCreateView(APIView):
    permission_classes = [IsAuthenticated,]


    def post(self, request):
        data = CommentSerializer(data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data, status=status.HTTP_201_CREATED)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)




class CommentUpdateView(APIView):
    permission_classes = [IsOwnerOrReadOnly,]


    def put(self, request, pk):
        commnet = Comment.objects.get(pk=pk)
        self.check_object_permissions(request, commnet)
        srz_data = CommentSerializer(instance=commnet, data=request.data, partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_201_CREATED)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDeleteView(APIView):
    permission_classes = [IsOwnerOrReadOnly,]


    def dlete(self, request, pk):
        post = Post.objects.get(pk=pk)
        self.check_object_permissions(request, post)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)