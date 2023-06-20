from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    # author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())


    class Meta:
        model = Post
        fields = ('title', 'header_image', 'title_tag', 'body','author')

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['author'] = request.user
        return super().create(validated_data)