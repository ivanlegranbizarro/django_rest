from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from posts.models import Post
from accounts.models import User


class PostListCreateViewTest(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username="testuser", email="testuser@testuser.com", password="testpassword"
        )
        self.url = reverse("posts:post-list-create-view")

    def test_list_posts(self):
        Post.objects.create(title="Post 1", content="Content 1")
        Post.objects.create(title="Post 2", content="Content 2")

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 2)

    def test_create_post(self):
        self.client.login(email=self.user.email, password=self.user.password)

        data = {"title": "New Post", "content": "This is my new post"}

        response = self.client.post(self.url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.last().title, "New Post")
