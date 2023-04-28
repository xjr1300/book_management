from typing import Type, Optional

from django import forms
from django.urls import reverse, reverse_lazy
from django.views import generic

from core.mixins import PageTitleMixin, FormActionMixin

from .models import Classification


class ClassificationViewMixin:
    """書籍分類ビューミックスイン"""

    model = Classification


class ClassificationSingleObjectMixin:
    """書籍分類ビューシングルオブジェクトミックスイン"""

    pk_url_kwarg = "code"


class ClassificationFormFieldMixin:
    """書籍分類フォームフィールドミックスイン"""

    fields = ("code", "name")


class ClassificationListView(ClassificationViewMixin, PageTitleMixin, generic.ListView):
    """書籍分類一覧クラスビュー"""

    title = "書籍分類一覧"


class ClassificationDetailView(
    ClassificationViewMixin,
    ClassificationSingleObjectMixin,
    PageTitleMixin,
    generic.DetailView,
):
    """書籍分類詳細クラスビュー"""

    title = "書籍分類詳細"


class ClassificationCreateView(
    ClassificationViewMixin,
    ClassificationFormFieldMixin,
    ClassificationSingleObjectMixin,
    PageTitleMixin,
    FormActionMixin,
    generic.CreateView,
):
    """書籍分類登録クラスビュー"""

    title = "書籍分類登録"
    action = "登録"

    def get_success_url(self) -> str:
        return reverse("books:classification-detail", kwargs={"code": self.object.code})


class ClassificationUpdateView(
    ClassificationViewMixin,
    ClassificationFormFieldMixin,
    ClassificationSingleObjectMixin,
    PageTitleMixin,
    FormActionMixin,
    generic.UpdateView,
):
    """書籍分類更新クラスビュー"""

    title = "書籍分類更新"
    action = "更新"

    def get_form(self, form_class: Optional[forms.Form] = None) -> forms.Form:
        form = super().get_form(form_class=form_class)
        form.fields["code"].widget.attrs["readonly"] = True
        return form

    def get_success_url(self) -> str:
        return reverse("books:classification-detail", kwargs={"code": self.object.code})


class ClassificationDeleteView(
    ClassificationViewMixin,
    ClassificationSingleObjectMixin,
    PageTitleMixin,
    generic.DeleteView,
):
    """書籍分類削除クラスビュー"""

    title = "書籍分類削除"
    success_url = reverse_lazy("books:classification-list")
