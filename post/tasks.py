from re import I
from .models import Post
from celery import shared_task



def all_post_list_objects_task():
    result = Post.get_objects()
    return result


@shared_task
def delete_object_task(key):
    Post.objects.filter(id=id).delete()



@shared_task
def download_object(key):
    Post.download_object(key)