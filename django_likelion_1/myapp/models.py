from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=100)
  content = models.TextField()
  pub_date = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return self.title

class Comment(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  content = models.CharField(max_length=100)
  pub_date = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return self.post.title + " / " + self.content

  class Meta:
    ordering = ['-id']