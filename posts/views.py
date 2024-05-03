from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response

from posts.models import Post
from posts.serializers import PostSerializer


class PostViewset(viewsets.ViewSet):
    def list(self, request):
        queryset = Post.objects.all()
        serializer = PostSerializer(instance=queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(instance=post)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
