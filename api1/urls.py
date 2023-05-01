from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns

from .books import views

urlpatterns = [
    path("books/classifications/", views.classification_list),
    path("books/classifications/<str:code>/", views.classification_detail),
]
