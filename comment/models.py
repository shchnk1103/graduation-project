from article.models import Article
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Comment(models.Model):
    parent = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='children'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    content = models.TextField()
    created = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.content[:20]
