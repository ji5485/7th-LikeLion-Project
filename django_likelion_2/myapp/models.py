from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  email = models.TextField()
  phone_number = models.TextField()
  like_posts = models.ManyToManyField('post.Post', blank=True, related_name="like_users") 
  
  def __str__(self):
    return self.user.username