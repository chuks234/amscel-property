from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views

app_name = "accounts"

urlpatterns = [
path(
"register/",
views.register,
name="register"
),


path(
    "login/",
    LoginView.as_view(
        template_name="accounts/login.html"
    ),
    name="login"
),

path(
    "logout/",
    LogoutView.as_view(),
    name="logout"
),

path(
    "dashboard/",
    views.dashboard,
    name="dashboard"
),

path(
    "review/",
    views.add_review,
    name="add_review"
),

path(
    "review/<int:review_id>/delete/",
    views.delete_review,
    name="delete_review"
),


]
