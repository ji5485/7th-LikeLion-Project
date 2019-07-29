from django.urls import path
from . import views

app_name = "post"
urlpatterns = [
  path('post_create/', views.post_create, name="post_create"),
  path('post_like_toggle/<int:post_id>', views.post_like_toggle, name="post_like_toggle")
]