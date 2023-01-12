from django.contrib.auth.models import Group
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_posts')
    group = models.ForeignKey(
    Group, on_delete=models.CASCADE, related_name='group_posts', blank=True, null=True
    )
    image = models.ImageField(upload_to='posts/', blank=True, null=True)
