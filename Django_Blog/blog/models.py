from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) #auto_now and auto_now_add can be used but not quite flexible(as the timezone will not change after the post was created).
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    #needed to not get error while creating posts
    def get_absolute_url(self):
        return reverse('post-detail' ,kwargs = {'pk' : self.pk})
    
