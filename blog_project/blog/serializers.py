# blog/serializers.py
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import BlogPost

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class BlogPostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content', 'author']
