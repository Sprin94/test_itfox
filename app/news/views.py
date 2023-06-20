from rest_framework.generics import (
    UpdateAPIView,
    ListCreateAPIView,
    DestroyAPIView,
    CreateAPIView,
)
from django.db.models import Count
from django.shortcuts import get_object_or_404

from news.serializers import NewsSerializer, CommentSerializer, LikeSerializer
from news.models import News, Comment, Like
from core.permissions import IsAuthorOrReadOnly, NewsAuthorCanDeleteComment


class NewsAPIView(UpdateAPIView, DestroyAPIView):
    serializer_class = NewsSerializer
    permission_classes = (IsAuthorOrReadOnly,)

    def get_queryset(self):
        return News.objects.annotate(
            count_likes=Count('likes'), count_comments=Count('comments')
        ).all()


class NewsListAPIView(NewsAPIView, ListCreateAPIView):
    serializer_class = NewsSerializer


class CommentListAPIView(ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class CommentAPIView(DestroyAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = (NewsAuthorCanDeleteComment,)


class LikeAPIView(DestroyAPIView, CreateAPIView):
    serializer_class = LikeSerializer
    queryset = Like.objects.all()

    def get_object(self):
        return get_object_or_404(Like, user=self.request.user, news__pk=self.kwargs.get('pk'))
