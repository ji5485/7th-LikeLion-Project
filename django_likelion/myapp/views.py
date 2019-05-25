from django.shortcuts import render, redirect
from .models import Post

# Create your views here.

def main(request):
  post_list = Post.objects.all()
  return render(request, 'main.html', {'post_list': post_list})

def detail(request, post_id):
  post = Post.objects.get(id=post_id)

  return render(request, 'detail.html', {'post': post})

def create(request):
  if request.method == "POST":
    post = Post()
    post.title = request.POST['title']
    post.content = request.POST['content']
    post.save()
    return redirect('main')

  else:
    return render(request, 'create.html')