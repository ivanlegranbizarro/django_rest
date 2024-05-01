from django.urls import path

from . import views

app_name = "posts"

urlpatterns = [
    path("", views.PostListCreateView.as_view(), name="all-posts-and-create"),
    path("detail/<str:id>", views.detail_post, name="detail-post"),
    path("delete/<str:id>", views.delete_post, name="delete-post"),
    path("update/<str:id>", views.update_post, name="update-post"),
]
