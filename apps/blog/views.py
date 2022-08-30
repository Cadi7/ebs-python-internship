from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from apps.blog.models import Category, Comments
from apps.blog.serializers import CategorySerializer, CommentSerializer
from apps.blog.models import Blog
from apps.blog.serializers import BlogSerializer

from drf_util.decorators import serialize_decorator
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CreateBlogView(GenericAPIView):
    serializer_class = BlogSerializer
    permission_classes = (AllowAny,)
    authentication_classes = ()


class BlogItemView(GenericAPIView):
    serializer_class = BlogSerializer, CommentSerializer

    permission_classes = (AllowAny,)
    authentication_classes = ()

    @staticmethod
    def get(request, pk):
        blog = get_object_or_404(Blog.objects.filter(pk=pk))
        comments = Comments.objects.all().filter(blog_id=pk)
        context = {
            'blog': BlogSerializer(blog).data,
            'comments': CommentSerializer(comments, many=True).data
        }
        return Response(context)


class BlogListView(GenericAPIView):
    serializer_class = BlogSerializer

    permission_classes = (AllowAny,)
    authentication_classes = ()

    @staticmethod
    def get(request):
        blogs = Blog.objects.all()

        return Response(BlogSerializer(blogs, many=True).data)

    @serialize_decorator(BlogSerializer)
    def post(self, request):
        validated_data = request.serializer.validated_data

        blog = Blog.objects.create(
            title=validated_data['title'],
            slug=validated_data['slug'],
            body=validated_data['body'],
            category=validated_data['category'],
            enabled=True
        )
        blog.save()

        return Response(BlogSerializer(blog).data)


class PostCommentView(GenericAPIView):
    serializer_class = CommentSerializer
    permission_classes = (AllowAny,)
    authentication_classes = ()

    @serialize_decorator(CommentSerializer)
    def post(self, request):
        validated_data = request.serializer.validated_data

        comment = Comments.objects.create(
            text=validated_data['title'],
            blog_id=validated_data['blog_id'])
        comment.save()

        return Response(CommentSerializer(comment).data)
