from django.urls import path

from . import views

app_name = "divisions"

urlpatterns = [
    # 部署一覧ページ(ex: /divisions/)
    path("", views.DivisionListView.as_view(), name="division-list"),
    # 部署登録ページ (ex: /divisions/create/)
    path("create/", views.create, name="division-create"),
    # 部署詳細ページ (ex: /divisions/<code>/)
    path("<str:code>/", views.DivisionDetailView.as_view(), name="division-detail"),
    # 部署更新ページ (ex: /divisions/update/<code>/)
    path("update/<str:code>/", views.update, name="division-update"),
    # 部署削除ページ (ex: /divisions/delete/<code>/)
    path("delete/<str:code>/", views.delete, name="division-delete"),
]
