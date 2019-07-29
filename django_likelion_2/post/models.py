from django.db import models
from myapp.models import Author

# Create your models here.
class Post(models.Model):
  author = models.ForeignKey(Author, on_delete=models.CASCADE)
  title = models.CharField(max_length=10)
  content = models.TextField()
  pub_date = models.DateTimeField(auto_now_add=True)
  edit_date = models.DateTimeField(auto_now=True)
  like_count = models.PositiveIntegerField(default=0)

  def __str__(self):
    return self.title