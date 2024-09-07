from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.blog.views import (
    BlogCreateView,
    BlogItemView,
    BlogListView,
    BlogWithCommentItemView,
    CategoryViewSet,
    CommentCreateView,
)

router = DefaultRouter(trailing_slash=False)
router.register(
    r"blog/categories",
    CategoryViewSet,
    basename="category",
)

urlpatterns = [
    path("blog", BlogListView.as_view(), name="blog_list"),
    path("blog/create", BlogCreateView.as_view(), name="blog_create"),
    path("blog/<int:pk>", BlogItemView.as_view(), name="blog_item"),
    path("blog/comments/create", CommentCreateView.as_view(), name="comment_create"),
    path("blog/blog/<int:pk>", BlogWithCommentItemView.as_view(), name="blog_comment_list"),
    *router.urls,
]
