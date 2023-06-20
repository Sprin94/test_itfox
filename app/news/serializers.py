from rest_framework.serializers import (
    ModelSerializer,
    HiddenField,
    CurrentUserDefault,
    IntegerField,
    SerializerMethodField,
)
from rest_framework.validators import UniqueTogetherValidator

from news.models import News, Comment, Like
from news.utils import NewsDefault


class CommentSerializer(ModelSerializer):
    author = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('date',)


class NewsSerializer(ModelSerializer):
    last_comments = SerializerMethodField()
    comments = IntegerField(source='count_comments', read_only=True)
    likes = IntegerField(source='count_likes', read_only=True)
    author = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = News
        fields = '__all__'

    def get_last_comments(self, obj) -> CommentSerializer(many=True):
        comments = obj.comments.order_by('-date').all()[:10]
        return CommentSerializer(comments, many=True).data


class LikeSerializer(ModelSerializer):
    user = HiddenField(default=CurrentUserDefault())
    news = HiddenField(default=NewsDefault())

    class Meta:
        model = Like
        fields = '__all__'
        validators = (
            UniqueTogetherValidator(
                queryset=Like.objects.all(),
                fields=('user', 'news'),
                message='Вы уже лайкнули эту новость'
            ),
        )
