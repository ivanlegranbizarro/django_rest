from django.urls import path

from . import views

app_name = "posts"

urlpatterns = [
    path("", views.PostListCreateView.as_view(), name="post-list-create-view"),
    path(
        "<str:id>",
        views.PostRetrieveUpdateDeleteView.as_view(),
        name="post-retrieve-update-delete-view",
    ),
]
