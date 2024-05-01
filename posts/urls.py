from django.urls import path

from . import views

app_name = "posts"

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("<str:id>", views.detail_post, name="detail-post"),
    path("create", views.create_post, name="create-post"),
    path("delete/<str:id>", views.delete_post, name="delete-post"),
    path("update/<str:id>", views.update_post, name="update-post"),
]
