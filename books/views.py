from typing import Optional

from django import forms
from django.urls import reverse, reverse_lazy
from django.views import generic

from core.mixins import FormActionMixin, PageTitleMixin

from .models import Classification, ClassificationDetail


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


class ClassificationDetailViewMixin:
    """書籍分類詳細ビューミックスイン"""

    model = ClassificationDetail


class ClassificationDetailSingleObjectMixin:
    """書籍分類詳細シングルオブジェクトミックスイン"""

    pk_url_kwarg = "code"
    context_object_name = "classification_detail"


class ClassificationDetailFormMixin(generic.edit.ModelFormMixin):
    """書籍分類詳細フォームフィールドミックスイン"""

    fields = ("code", "classification", "name")
    template_name = "books/classification_detail_form.html"

    def get_form(self, form_class: Optional[forms.Form] = None) -> forms.Form:
        form = super().get_form(form_class)
        form.fields["classification"].empty_label = None
        return form


class ClassificationDetailListView(
    ClassificationDetailViewMixin, PageTitleMixin, generic.ListView
):
    """書籍分類詳細一覧クラスビュー"""

    title = "書籍分類詳細一覧"
    context_object_name = "classification_detail_list"
    template_name = "books/classification_detail_list.html"


class ClassificationDetailDetailView(
    ClassificationDetailViewMixin,
    ClassificationDetailSingleObjectMixin,
    PageTitleMixin,
    generic.DetailView,
):
    """書籍分類詳細詳細クラスビュー"""

    title = "書籍分類詳細詳細"
    template_name = "books/classification_detail_detail.html"


class ClassificationDetailCreateView(
    ClassificationDetailViewMixin,
    ClassificationDetailFormMixin,
    ClassificationDetailSingleObjectMixin,
    PageTitleMixin,
    FormActionMixin,
    generic.CreateView,
):
    """書籍分類詳細登録クラスビュー"""

    title = "書籍分類詳細登録"
    action = "登録"

    def get_success_url(self) -> str:
        return reverse(
            "books:classification-detail-detail", kwargs={"code": self.object.code}
        )


class ClassificationDetailUpdateView(
    ClassificationDetailViewMixin,
    ClassificationDetailFormMixin,
    ClassificationDetailSingleObjectMixin,
    PageTitleMixin,
    FormActionMixin,
    generic.UpdateView,
):
    """書籍分類詳細更新クラスビュー"""

    title = "書籍分類詳細更新"
    action = "更新"

    def get_form(self, form_class: Optional[forms.Form] = None) -> forms.Form:
        form = super().get_form(form_class=form_class)
        form.fields["code"].widget.attrs["readonly"] = True
        return form

    def get_success_url(self) -> str:
        return reverse(
            "books:classification-detail-detail", kwargs={"code": self.object.code}
        )


class ClassificationDetailDeleteView(
    ClassificationDetailViewMixin,
    ClassificationDetailSingleObjectMixin,
    PageTitleMixin,
    generic.DeleteView,
):
    """書籍分類詳細削除クラスビュー"""

    title = "書籍分類詳細削除"
    template_name = "books/classification_detail_confirm_delete.html"
    success_url = reverse_lazy("books:classification-detail-list")
