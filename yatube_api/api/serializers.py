from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
<<<<<<< HEAD
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Comment, Follow, Group, Post, User
=======


from posts.models import Comment, Post
>>>>>>> 5596f616f928223a336f7372d31359f311bf4a2c


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


<<<<<<< HEAD
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Group


class CommentSerializer(serializers.ModelSerializer):
    post = serializers.ReadOnlyField(source='post.id')
=======
class CommentSerializer(serializers.ModelSerializer):
>>>>>>> 5596f616f928223a336f7372d31359f311bf4a2c
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment
<<<<<<< HEAD


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )

    class Meta:
        fields = ('user', 'following')
        model = Follow
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=['user', 'following']
            )
        ]

    def validate(self, data):
        """Проверяем, что не подписываемся на самого себя."""
        if self.context['request'].user != data.get('following'):
            return data
        raise serializers.ValidationError("Нельзя подписаться на самого себя")
=======
>>>>>>> 5596f616f928223a336f7372d31359f311bf4a2c
