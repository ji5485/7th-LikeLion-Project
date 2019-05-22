from django.shortcuts import render
from .models import Post

# Create your views here.

def main(request):
  post_list = Post.objects.all()
  return render(request, 'main.html', {'post_list': post_list})