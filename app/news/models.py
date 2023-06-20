from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class News(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    text = models.TextField('Текст')
    author = models.ForeignKey(
        User, verbose_name='Автор', on_delete=models.PROTECT, related_name='news'
    )
    date = models.DateField('Дата')


class Comment(models.Model):
    news = models.ForeignKey(
        News, on_delete=models.CASCADE, verbose_name='Новость', related_name='comments'
    )
    date = models.DateTimeField('Дата создания', auto_now_add=True)
    author = models.ForeignKey(
        User, verbose_name='Автор', on_delete=models.PROTECT, related_name='comments'
    )
    text = models.TextField('Текст')


class Like(models.Model):
    news = models.ForeignKey(
        News, on_delete=models.PROTECT, verbose_name='Новость', related_name='likes'
    )
    user = models.ForeignKey(
        User, verbose_name='Пользователь', on_delete=models.PROTECT, related_name='likes'
    )

    class Meta:
        constraints = (
            models.UniqueConstraint(fields=('user', 'news'), name='unique_like'),
        )
