from django.shortcuts import render, redirect
from .models import Post
from myapp.models import Author

# Create your views here.
def post_create(request):
  if request.method == "POST":
    title, content = request.POST.get('title'), request.POST.get('content')
    
    author = Author.objects.get(user=request.user)
    post = Post(author=author, title=title, content=content)
    post.save()

    return redirect("main")
  else:
    return render(request, "post/post_create.html")

def post_like_toggle(request, post_id):
  post = Post.objects.get(id=post_id)
  user = request.user
  author = user.author

  check_like_post = author.like_post.filter(id=post_id)
  if check_like_post.exists():
    author.like_posts.remove(post)
    post.like_count -= 1
    post.save()
  else:
    author.like_posts.add(post)
    post.like_count += 1
    post.save()

  return redirect("main")