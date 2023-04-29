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
    # 書籍分類詳細一覧ページ(ex: /classification-details/)
    path(
        "classification-details/",
        views.ClassificationDetailListView.as_view(),
        name="classification-detail-list",
    ),
    # 書籍分類詳細登録ページ (ex: /classification-details/create/)
    path(
        "classification-details/create/",
        views.ClassificationDetailCreateView.as_view(),
        name="classification-detail-create",
    ),
    # 書籍分類詳細詳細ページ (ex: /classification-details/<code>/)
    path(
        "classification-details/<str:code>/",
        views.ClassificationDetailDetailView.as_view(),
        name="classification-detail-detail",
    ),
    # 書籍分類詳細更新ページ (ex: /classification-details/update/<code>/)
    path(
        "classification-details/update/<str:code>/",
        views.ClassificationDetailUpdateView.as_view(),
        name="classification-detail-update",
    ),
    # 書籍分類詳細削除ページ (ex: /classification-details/delete/<code>/)
    path(
        "classification-details/delete/<str:code>/",
        views.ClassificationDetailDeleteView.as_view(),
        name="classification-detail-delete",
    ),
    # 書籍一覧ページ (ex: /books/)
    path("", views.BookListView.as_view(), name="book-list"),
    # 書籍登録ページ (ex: /books/create/)
    path("create/", views.BookCreateView.as_view(), name="book-create"),
    # 書籍詳細ページ (ex: /books/<id>/)
    path("<str:pk>/", views.BookDetailView.as_view(), name="book-detail"),
    # 書籍更新ページ (ex: /books/update/<id>/)
    path("update/<str:pk>/", views.BookUpdateView.as_view(), name="book-update"),
]
