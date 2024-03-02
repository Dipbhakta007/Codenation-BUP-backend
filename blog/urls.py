from django.urls import path
from blog.views import (
     PostList,
     PostDetail
)

urlpatterns = [
    path('posts/', PostList.as_view()),
    path('posts/<int:pk>/', PostDetail.as_view()),
]