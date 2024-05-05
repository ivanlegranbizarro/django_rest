from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.request import Request

from posts.permissions import OnlyOwnerCanEditOrDelete

from .models import Post
from .serializers import PostSerializer
from rest_framework.pagination import PageNumberPagination


class CustomPaginator(PageNumberPagination):
    page_size = 3
    page_query_param = "page"
    page_size_query_param = "page_size"


class PostForCurrentUserView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        current_user = self.request.user

        return Post.objects.filter(author=current_user)


class PostListCreateView(
    generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin
):
    serializer_class = PostSerializer
    permission_classes = [AllowAny]
    pagination_class = CustomPaginator
    queryset = Post.objects.all().order_by("-created_at")

    def get(self, request: Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request: Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PostUpdateRetrieveDeleteView(
    generics.GenericAPIView,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
):

    serializer_class = PostSerializer
    permission_classes = [
        OnlyOwnerCanEditOrDelete,
    ]
    queryset = Post.objects.all()

    def get(self, request: Request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request: Request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request: Request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
