from statistics import mode
from django.db import models
from post.models import CustomUser
from django.utils.text import slugify
from post.models import Post
# Create your models here.



class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comment')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    slug = models.SlugField(max_length=200, unique=True)
    upload_on = models.DateTimeField(auto_now= True)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    repaly = models.ForeignKey('Comment', on_delete=models.CASCADE, related_name="replies", null=True)
    

    class Meta:
        ordering = ['-created_on']




    def __str__(self):
        return f'{self.user}-{self.description[:10]}'


    def save(self, *args, **kwargs):
        self.slug = slugify(self.description[:10])
        super().save(*args, **kwargs)





 