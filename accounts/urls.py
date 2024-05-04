from django.urls import path

from accounts import views

app_name = "auth"

urlpatterns = [
    path("all-users", views.ListOfAllUsers.as_view(), name="all-users"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("login/", views.LoginView.as_view(), name="login"),
]
