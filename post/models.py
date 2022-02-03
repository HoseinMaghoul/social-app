from email.mime import image
from email.policy import default
from statistics import mode
from django.db import models
from users.models import CustomUser
from django.utils.text import slugify
# Create your models here.

STATUS = (
    (0, 'Draft'),
    (1, 'Pulish')
)



class Post(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='blog_posts')
    slug = models.SlugField(max_length=200, unique=True)
    title = models.CharField(max_length=200)
    upload_on = models.DateTimeField(auto_now= True)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    


    class Meta:
        ordering = ['-created_on']

    
    def __str__(self):
        return self.title

    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        