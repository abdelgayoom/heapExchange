from blog.models import Posts, Comments
from rest_framework import serializers


class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = '__all__'

