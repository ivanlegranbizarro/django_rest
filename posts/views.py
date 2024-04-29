from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from .serializers import PostSerializer
from .models import Post


@api_view(["GET"])
def homepage(request: Request) -> Response:
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
