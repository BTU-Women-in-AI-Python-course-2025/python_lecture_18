from rest_framework import serializers
from blog.models import BlogPost, BlogPostCover


class BlogPostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'created_at', 'category']


class BlogPostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'text', 'created_at', 'category', 'website', 'document']


class BlogPostCreateUpdateSerializer(serializers.ModelSerializer):
    cover = serializers.ImageField(required=False)

    class Meta:
        model = BlogPost
        fields = ['title', 'text', 'category', 'website', 'document', 'cover']

    def create(self, validated_data):
        cover = validated_data.pop('cover', None)
        blog_post = BlogPost.objects.create(**validated_data)
        if cover:
            BlogPostCover.objects.create(blog_post=blog_post, image=cover)
        return blog_post

    def update(self, instance, validated_data):
        cover = validated_data.pop('cover', None)
        BlogPost.objects.filter(id=instance.id).update(**validated_data)
        blog_post_cover = BlogPostCover.objects.filter(blog_post=instance)
        if blog_post_cover.exists():
            cover_instance = blog_post_cover.first()
            cover_instance.image = cover
            cover_instance.save()
        else:
            BlogPostCover.objects.create(blog_post=instance, image=cover)
        return instance
