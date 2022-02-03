from  rest_framework.views import APIView
from . serializers import PostSerializer
from rest_framework.response import Response
from rest_framework import status 
from . models import Post
from rest_framework.permissions import IsAuthenticated
from permissions import IsOwnerOrReadOnly



class PostListView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        srz_data = PostSerializer(instance=posts, many=True)
        return Response(srz_data, status=status.HTTP_200_ok)



class PostCreateView(APIView):
    permission_classes = [IsAuthenticated,]


    def post(self, request):
        data = PostSerializer(data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data, status=status.HTTP_201_CREATED)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)



class PostUpdateView(APIView):
    permmission_classes = [IsAuthenticated,]


    def put(self, request, pk):
        post = Post.objects.get(pk=pk)
        self.check_object_permissions(request, post)
        srz_data = PostSerializer(instance=post, data=request.data, partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_201_CREATED)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)




class PostDeleteView(APIView):
    permiision_classes = [IsAuthenticated,]


    def delete(self, request, pk):
        post = Post.objects.get(pk=pk)
        self.check_objects_permissions(request, post)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
        