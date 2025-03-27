from django.contrib.auth import get_user_model
from django.db import models
<<<<<<< HEAD
from django.db.models import F, Q
=======
>>>>>>> 5596f616f928223a336f7372d31359f311bf4a2c

User = get_user_model()


<<<<<<< HEAD
class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title


=======
>>>>>>> 5596f616f928223a336f7372d31359f311bf4a2c
class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
<<<<<<< HEAD
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name='posts',
        blank=True, null=True, )
=======
>>>>>>> 5596f616f928223a336f7372d31359f311bf4a2c
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True)

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)
<<<<<<< HEAD

    def __str__(self):
        return self.text


class Follow(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='follower')
    following = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='following')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'following'],
                name='unique_follow'),
            models.CheckConstraint(
                check=~Q(user=F('following')),
                name='user_not_following')
        ]

    def __str__(self):
        return f'{self.user.username} подписан на {self.following.username}'
=======
>>>>>>> 5596f616f928223a336f7372d31359f311bf4a2c
