from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from .models import Author
from django.contrib import auth
from django.contrib.auth.hashers import check_password

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

      email = request.POST.get('email')
      phone_number = request.POST.get('phone_number')
      author = Author(user=user, email=email, phone_number=phone_number)
      author.save()
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

def logout(request):
  auth.logout(request)
  return redirect('main')

def change_pw(request):
  if request.method == "POST":
    origin_password = request.POST.get('origin_password')
    user = request.user

    if check_password(origin_password, user.password):
      password1 = request.POST.get('password1')
      password2 = request.POST.get('password2')

      if password1 == password2:
        user.set_password(password1)
        user.save()
        auth.login(request, user)

        return redirect("main")

      else:
        return HttpResponse("비밀번호가 틀렸습니다")

    else:
      return HttpResponse("기존의 비밀번호를 다시 확인하세요")
      
  else:
    return render(request, "myapp/change_pw.html")