from django.urls import path

from . import views

app_name = "accounts"

urlpatterns = [
    # ログインページ
    path("login/", views.LoginView.as_view(), name="login"),
    # ログアウトページ
    path("logout/", views.LogoutView.as_view(), name="logout"),
]
