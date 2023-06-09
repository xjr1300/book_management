from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .books import views

urlpatterns = [
    path("books/classifications/", views.classification_list),
    path("books/classifications/<str:code>/", views.classification_detail),
    path(
        "books/classification-details/",
        views.ClassificationDetailListCreateView.as_view(),
    ),
    path(
        "books/classification-details/<str:code>/",
        views.ClassificationRetrieveUpdateDestroyView.as_view(),
    ),
    path("auth/token/", TokenObtainPairView.as_view()),
    path("auth/token/refresh/", TokenRefreshView.as_view()),
]


# 書籍ビューセットをディスパッチ
router = DefaultRouter()
router.register("books", viewset=views.BookViewSet)
urlpatterns += router.urls
