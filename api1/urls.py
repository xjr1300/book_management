from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns

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
]
