from django.urls import path

from apps.blog.views import CategoryViewSet, BlogListView, BlogItemView, CreateBlogView, PostCommentView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')


urlpatterns = router.urls

urlpatterns += [
    path('', BlogListView.as_view(), name='blog_list'),
    path('commments/', PostCommentView.as_view(), name='comments'),
    path('<int:pk>/', BlogItemView.as_view(), name='blog_item'),
    # path('create/', CreateBlogView.as_view(), name='blog')
]
