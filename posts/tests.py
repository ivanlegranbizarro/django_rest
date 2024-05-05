from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from posts.models import Post
from accounts.models import User
from rest_framework_simplejwt.tokens import RefreshToken


class PostListCreateViewTest(APITestCase):
    def setUp(self):
        # Crear un usuario y obtener un JWT
        self.user = User.objects.create_user(
            username="testuser", email="testuser@testuser.com", password="testpassword"
        )

        # Obtener el token JWT
        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)

        # Configurar la URL para la vista que vas a probar
        self.url = reverse("posts:post-list-create-view")

    def test_list_posts(self):
        # Autenticar usando el token
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.access_token}")

        # Crear algunos posts para verificar el listado
        Post.objects.create(title="Post 1", content="Content 1")
        Post.objects.create(title="Post 2", content="Content 2")

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 2)

    def test_create_post(self):
        # Autenticar usando el token
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.access_token}")

        data = {
            "title": "New Post",
            "content": "This is my new post",
            "author": self.user.id,
        }

        response = self.client.post(self.url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.last().title, "New Post")
