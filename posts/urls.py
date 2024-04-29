from django.urls import path

from . import views

app_name = "posts"

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("<str:id>", views.detail_post, name="detail-post"),
    path("create-post", views.create_post, name="create-post"),
]
