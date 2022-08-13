from django.contrib.auth.models import User
from rest_framework import serializers

from apps.blog.models import Category, Blog, Comments


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ("id", "title", "slug", "body", "posted", "category", "enabled",)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ("id", "text", "blog_id", )
