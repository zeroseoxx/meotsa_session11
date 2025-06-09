from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta: #클래의 설정값 = 메타 데이터 
        model = Post
        fields = ['id', 'user', 'title', 'body']