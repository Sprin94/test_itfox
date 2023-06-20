from django.urls import path

from news.views import (
    NewsAPIView,
    CommentAPIView,
    NewsListAPIView,
    CommentListAPIView,
    LikeAPIView,
)

app_name = 'news'

urlpatterns = [
    path('news/', NewsListAPIView.as_view()),
    path('news/<int:pk>/', NewsAPIView.as_view()),
    path('news/<int:pk>/like/', LikeAPIView.as_view()),
    path('comments/', CommentListAPIView.as_view()),
    path('comments/<int:pk>/', CommentAPIView.as_view()),
]
