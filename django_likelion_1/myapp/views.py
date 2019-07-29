from django.shortcuts import render, redirect
from .models import Post, Comment
from .form import PostForm, CommentForm

# Create your views here.

def main(request):
  post_list = Post.objects.all()
  context = {
    'post_list': post_list
  }
  return render(request, 'main.html', context)

def detail(request, post_id):
  post = Post.objects.get(id=post_id)
  comment_list = Comment.objects.filter(post=post)
  form = CommentForm()

  return render(request, 'detail.html', {'post': post, 'comment_list': comment_list, 'form': form})

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

def comment_create(request, post_id):
  if request.method == "POST":
    post = Post.objects.get(id=post_id)
    comment = Comment(post=post)
    comment.content = request.POST['content']
    comment.save()
    return redirect('detail', post_id)

def comment_delete(request, comment_id):
  comment = Comment.objects.get(id=comment_id)
  post_id = comment.post.id
  comment.delete()
  return redirect('detail', post_id)