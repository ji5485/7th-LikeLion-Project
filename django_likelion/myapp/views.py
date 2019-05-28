from django.shortcuts import render, redirect
from .models import Post
from .form import PostForm

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
    form = PostForm()
    return render(request, 'create.html', {'form': form})

def delete(request, post_id):
  post = Post.objects.get(id=post_id)
  post.delete()
  return redirect('main')

def update(request, post_id):
  post = Post.objects.get(id=post_id)

  if request.method == "POST":
    post.title = request.POST['title']
    post.content = request.POST['content']
    post.save()
    return render(request, 'detail.html', {'post': post})
  else:
    form = PostForm(instance=post)
    return render(request, 'update.html', {'form': form})