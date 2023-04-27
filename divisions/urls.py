from django.urls import path

from . import views

app_name = "divisions"

urlpatterns = [
    # 部署一覧ページ(ex: /divisions/)
    path("", views.list, name="division-list"),
]
