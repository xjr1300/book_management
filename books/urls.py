from django.urls import path

from . import views

app_name = "books"

urlpatterns = [
    # 書籍分類一覧ページ(ex: /classifications/)
    path(
        "classifications/",
        views.ClassificationListView.as_view(),
        name="classification-list",
    ),
    # 書籍分類登録ページ (ex: /classifications/create/)
    path(
        "classifications/create/",
        views.ClassificationCreateView.as_view(),
        name="classification-create",
    ),
    # 書籍分類詳細ページ (ex: /classifications/<code>/)
    path(
        "classifications/<str:code>/",
        views.ClassificationDetailView.as_view(),
        name="classification-detail",
    ),
    # 書籍分類更新ページ (ex: /classifications/update/<code>/)
    path(
        "classifications/update/<str:code>/",
        views.ClassificationUpdateView.as_view(),
        name="classification-update",
    ),
    # 書籍分類削除ページ (ex: /classifications/delete/<code>/)
    path(
        "classifications/delete/<str:code>/",
        views.ClassificationDeleteView.as_view(),
        name="classification-delete",
    ),
]
