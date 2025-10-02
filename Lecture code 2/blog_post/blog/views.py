from rest_framework import mixins, viewsets
from rest_framework.viewsets import ModelViewSet

from blog.models import BlogPost
from blog.serializers import (
    BlogPostListSerializer,
    BlogPostDetailSerializer,
    BlogPostCreateUpdateSerializer
)

class BlogPostListViewSet(mixins.ListModelMixin,
                         viewsets.GenericViewSet):
    queryset = BlogPost.objects.filter(deleted=False)
    serializer_class = BlogPostListSerializer


class BlogPostDetailViewSet(mixins.RetrieveModelMixin,
                            viewsets.GenericViewSet):
    queryset = BlogPost.objects.filter(deleted=False)
    serializer_class = BlogPostDetailSerializer


class BlogPostUpdateViewSet(mixins.UpdateModelMixin,
                            viewsets.GenericViewSet):
    queryset = BlogPost.objects.filter(deleted=False)
    serializer_class = BlogPostCreateUpdateSerializer


class BlogPostCreateViewSet(mixins.CreateModelMixin,
                            viewsets.GenericViewSet):
    queryset = BlogPost.objects.filter(deleted=False)
    serializer_class = BlogPostCreateUpdateSerializer


class  BlogPostDeleteViewSet(mixins.DestroyModelMixin,
                             viewsets.GenericViewSet):
    queryset = BlogPost.objects.filter(deleted=False)
    serializer_class = BlogPostListSerializer


class BlogPostViewSet(ModelViewSet):
    queryset = BlogPost.objects.filter(deleted=False)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return BlogPostDetailSerializer
        elif self.action == 'create' or self.action == 'update':
            return BlogPostCreateUpdateSerializer
        else:
            return BlogPostListSerializer
