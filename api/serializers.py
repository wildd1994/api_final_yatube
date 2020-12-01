from rest_framework import serializers

from .models import Comment, Follow, Group, Post, User


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = ('id', 'text', 'author', 'pub_date')
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = ('id', 'author', 'post', 'text', 'created')
        model = Comment


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('title', 'id')
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    following = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())

    def validate_following(self, value):
        user = self.context['request'].user
        is_follow = Follow.objects.filter(user=user, following=value).exists()
        if is_follow:
            raise serializers.ValidationError('Вы уже подписаны на этого пользователя')
        if user == value:
            raise serializers.ValidationError('Нельзя подписаться на себя')
        return value

    class Meta:
        fields = ('user', 'following')
        model = Follow

