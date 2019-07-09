from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def main(request):
  return render(request, "myapp/main.html")

def signup(request):
  if request.method == "POST":
    username = request.POST.get('username')
    password1 = request.POST.get('password1')
    password2 = request.POST.get('password2')

    if password1 == password2:
      user = User.objects.create_user(username=username, password=password1)
    else:
      pass

    return redirect('main')
  return render(request, "myapp/signup.html")

def login(request):
  if request.method == "POST":
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    user = auth.authenticate(request, username=username, password=password)

    if user is not None:
      auth.login(request, user)
      return redirect('main')
    else:
      # 유저가 없는 경우
      pass

    return redirect('login')
  return render(request, "myapp/login.html")
