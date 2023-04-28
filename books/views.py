from typing import Any, Dict, Optional

from django import forms
from django.db.models import QuerySet
from django.http import HttpRequest
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


def get_classification_from_param(request: HttpRequest) -> Optional[Classification]:
    """GETパラメータで指定された書籍分類コードから書籍分類モデルインスタンスを取得して返却する。

    Args:
        request: HTTPリクエスト

    Returns
        書籍分類モデルインスタンス。
        GETパラメーターに書籍分類コードが指定されていない場合、またそのパラメータで指定された書籍分類コードと
        一致する書籍分類が存在しない場合はNone。
    """
    # 書籍分類コードを取得
    code = request.GET.get("classification_code", None)
    # 書籍分類コードが指定されていない場合はNoneを返却
    if not code:
        return None

    try:
        # 書籍分類コードから書籍分類モデルインスタンスを取得
        return Classification.objects.get(code=code)
    except Classification.DoesNotExist:
        # 書籍分類コードから書籍分類モデルインスタンスを取得できない場合はNoneを返却
        return None


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
    # 書籍分類詳細をフィルタする書籍分類
    classification: Optional[Classification] = None

    def get_queryset(self) -> QuerySet[ClassificationDetail]:
        """書籍分類詳細一覧ページで表示する書籍分類詳細QuerySetを返却する。"""
        self.classification = get_classification_from_param(self.request)
        if not self.classification:
            return ClassificationDetail.objects.all()
        else:
            return ClassificationDetail.objects.filter(
                classification=self.classification
            )

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        """コンテキストを返却する。

        コンテキストを取得して、コンテキストにすべての書籍分類詳細モデルインスタンスと、
        書籍分類詳細をフィルタする書籍分類モデルインスタンスを登録する。
        """
        # コンテキストを取得
        ctx = super().get_context_data(**kwargs)
        # コンテキストにすべての書籍分類詳細モデルインスタンスを登録
        ctx["classification_list"] = Classification.objects.all()
        # コンテキストに書籍分類詳細をフィルタする書籍分類モデルインスタンスを登録
        ctx["current_classification"] = self.classification
        return ctx


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
