from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializer


@api_view(["GET"])
def all_posts(request: Request) -> Response:
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
def create_post(request: Request) -> Response:
    """
    Creates a new Post object based on the request data.
    """
    serializer = PostSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()  # Save the serialized data to create a new Post object
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def detail_post(request: Request, id: str) -> Response:
    """
    Search for a specific post using the id parameter
    """
    post = get_object_or_404(Post, pk=id)
    serializer = PostSerializer(post)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["DELETE"])
def delete_post(request: Request, id: str) -> Response:
    post = get_object_or_404(Post, pk=id)
    post.delete()

    return Response(
        {"message": "Post was deleted successfully"}, status=status.HTTP_204_NO_CONTENT
    )


@api_view(["PUT"])
def update_post(request: Request, id: str) -> Response:
    post = get_object_or_404(Post, pk=id)
    serializer = PostSerializer(post, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
