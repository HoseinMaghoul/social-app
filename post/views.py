from urllib import request
from django.shortcuts import render, redirect
from django.views import View
from permissions import IsSuperUserMixin
from .models import Post
from . tasks import all_post_list_objects_task, delete_object_task
from django.contrib import messages

# Create your views here.




class PostList(IsSuperUserMixin, View):
    template_name = 'post/index.html'


    def get(self, request):
        posts = Post.objects.all()
        return render(request, self.template_name, {'posts':posts})
    # queryset = Post.objects.filter(status=1).order_by('-created_on')



class PostDelete(IsSuperUserMixin, View):
    def get(self, request,p_id):
        delete_object_task(p_id)
        messages.success(request, 'your request will done soon!', 'ino')
        return redirect('post:index' )
    


class PostDownload(IsSuperUserMixin, View):
    def get(self, request, key):
        # delete_object_task.delay(key)
        # messages.success(request, 'your download will start soon', 'info')
        # return redirect('post:index')
        pass